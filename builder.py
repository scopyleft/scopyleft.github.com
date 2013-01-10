#!/usr/bin/env python

"""XXX: expliquer pourquoi c'est publiquement accessible en HTTP sur github"""

import locale
import os

from argh import *
from datetime import datetime
from fabric.api import local

from flask import Flask, render_template
from flask_frozen import Freezer
from flaskext.flatpages import FlatPages
from flaskext.markdown import Markdown
from flaskext.assets import Environment as AssetManager

# Configuration
DEBUG = False
BASE_URL = 'https://scopyleft.fr'
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
SOURCES_DIR = os.path.join(ROOT_DIR, 'sources')
STATIC_DIR = os.path.join(SOURCES_DIR, 'static')
TEMPLATES_DIR = os.path.join(SOURCES_DIR, 'templates')
ASSETS_DEBUG = DEBUG
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = os.path.join(SOURCES_DIR, 'pages')
FREEZER_DESTINATION = ROOT_DIR
FREEZER_REMOVE_EXTRA_FILES = False # to keep git related stuff in there

# App configuration
FEED_MAX_LINKS = 25
SECTION_MAX_LINKS = 12

app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
markdown_manager = Markdown(app)
asset_manager = AssetManager(app)


@app.template_filter()
def to_rfc2822(dt):
    if not dt:
        return
    current_locale = locale.getlocale(locale.LC_TIME)
    locale.setlocale(locale.LC_TIME, "en_US")
    formatted = dt.strftime("%a, %d %b %Y %H:%M:%S +0000")
    locale.setlocale(locale.LC_TIME, current_locale)
    return formatted


def discover_urls():
    return [('page', dict(path=page.path)) for page in pages]


def get_blog_posts(pages, limit=None):
    posts = sorted([p for p in pages if p.path.startswith('blog')],
        key=lambda p: p.meta.get('date'), reverse=True)
    return posts[:limit] if limit is not None else posts


@app.route('/')
def index():
    return render_template('page.html', page=pages.get_or_404('homepage'))


@app.route('/blog/')
def blog():
    return render_template('blog.html', pages=get_blog_posts(pages))


@app.route('/syndication/')
def feed():
    return render_template('base.rss', build_date=datetime.now(),
        pages=get_blog_posts(pages, limit=FEED_MAX_LINKS))


@app.route('/<path:path>/')
def page(path):
    template = 'post.html' if path.startswith('blog') else 'page.html'
    return render_template(template, page=pages.get_or_404(path))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@command
def build():
    """ Builds this site.
    """
    print("Building website...")
    app.debug = False
    asset_manager.config['ASSETS_DEBUG'] = False
    freezer.freeze()
    local("cp ./sources/static/*.ico ./static/")
    local("cp ./sources/static/*.txt ./static/")
    local("cp ./sources/static/CNAME ./static/")
    print("Done.")


@command
def serve(server='127.0.0.1', port=5000, debug=DEBUG):
    """ Serves this site.
    """
    asset_manager.config['ASSETS_DEBUG'] = debug
    if debug:
        app.debug = True
    app.run(host=server, port=port, debug=debug)


if __name__ == '__main__':
    freezer.register_generator(discover_urls)
    parser = ArghParser()
    parser.add_commands([build, serve, ])
    parser.dispatch()
