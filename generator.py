import locale
import os
from dataclasses import dataclass
from datetime import datetime
from html import escape
from pathlib import Path

import frontmatter
import minicli
import mistune
from jinja2 import Environment as Env
from jinja2 import FileSystemLoader
from slugify import slugify

__version__ = "0.0.1"

HERE = Path().resolve()
BLOG = HERE / "blog"
# Utile pour le rendu des langues en français.
locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")
NORMALIZED_STRFTIME = "%Y-%m-%dT12:00:00+01:00"
TODAY = datetime.today()

# Pour que Jinja2 sache où trouver les fichiers de templates.
environment = Env(loader=FileSystemLoader(str(HERE / "templates")))

# Le convertisseur markdown avec l’activation des plugins utiles.
md = mistune.create_markdown(
    plugins=["strikethrough", "table", "url", "task_lists"],
    escape=False,
    hard_wrap=True,
)


@dataclass
class BlogPost:
    item: dict
    markdown: str
    html: str
    file_path: str

    def __post_init__(self):
        # Méta-données obligatoires.
        self.titre = self.item["titre"]
        self.titre_escape = escape(self.titre)
        self.date_publication = self.item["date_publication"]
        self.year = self.date_publication.year
        self.slug = slugify(self.titre)
        # Construction de l’URL unique pour cet article.
        self.url = f"/blog/{self.year}/{self.slug}/"
        self.full_url = f"http://scopyleft.fr{self.url}"
        self.normalized_date = self.date_publication.strftime(NORMALIZED_STRFTIME)
        self.escaped_content = escape(self.html)

    def __eq__(self, other):
        return self.url == other.url

    def __lt__(self, other: "BlogPost"):
        if not isinstance(other, BlogPost):
            return NotImplemented
        return self.date_publication < other.date_publication

    @staticmethod
    def all(source: Path):
        items = []
        for folder in each_folder_from(source):
            for subfolder in each_folder_from(folder):
                for markdown_file in each_file_from(subfolder, pattern="*.md"):
                    item = frontmatter.load(markdown_file)
                    html = md(item.content)
                    page = BlogPost(
                        item=item,
                        markdown=item.content,
                        html=html,
                        file_path=markdown_file.name,
                    )
                    items.append(page)
        return sorted(items, reverse=True)


@minicli.cli
def build():
    template_blogpost = environment.get_template("blogpost.html")
    template_blogposts = environment.get_template("blogposts.html")

    # On récupère toutes les blogposts.
    blogposts = BlogPost.all(source=BLOG)

    # Page d’accueil avec les derniers items.
    content = template_blogposts.render(blogposts=blogposts)
    Path(BLOG / "index.html").write_text(content)

    # Page de détail d’un blogpost.
    for blogpost in blogposts:
        content = template_blogpost.render(blogpost=blogpost)
        target_path = Path(BLOG / str(blogpost.year) / blogpost.slug)
        target_path.mkdir(parents=True, exist_ok=True)
        Path(target_path / "index.html").write_text(content)


@minicli.cli
def feed():
    """Generate a feed from last published items."""
    template = environment.get_template("feed.xml")

    # On récupère toutes les blogposts.
    blogposts = BlogPost.all(source=BLOG)

    content = template.render(
        blogposts=blogposts,
        current_dt=TODAY.strftime(NORMALIZED_STRFTIME),
        BASE_URL="http://scopyleft.fr",
    )
    (HERE / "syndication" / "flux.atom").write_text(content)


# Des utilitaires pour parcourir les fichiers markdown des sujets.


def each_file_from(source_dir, pattern="*", exclude=None):
    """Walk across the `source_dir` and return the `pattern` file paths."""
    for path in _each_path_from(source_dir, pattern=pattern, exclude=exclude):
        if path.is_file():
            yield path


def _each_path_from(source_dir, pattern="*", exclude=None):
    for path in sorted(Path(source_dir).glob(pattern)):
        if exclude is not None and path.name in exclude:
            continue
        yield path


def each_folder_from(source_dir, exclude=None):
    """Walk across the `source_dir` and return the folder paths."""
    for direntry in os.scandir(source_dir):
        if direntry.is_dir():
            if exclude is not None and direntry.name in exclude:
                continue
            yield direntry


if __name__ == "__main__":
    minicli.run()
