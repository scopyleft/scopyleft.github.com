#!/usr/bin/env python

import os

from argh import *
from fabric.api import local
from flask import Flask, render_template
from flask_frozen import Freezer
from flaskext.flatpages import FlatPages
from flaskext.markdown import Markdown
from flaskext.assets import Environment as AssetManager

# Configuration
DEBUG = False
BASE_URL = 'https://scopyleft.fr'
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
ASSETS_DEBUG = DEBUG
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'pages'
FREEZER_DESTINATION = 'master'
FREEZER_REMOVE_EXTRA_FILES = False # to keep git related stuff in there

# App configuration
FEED_MAX_LINKS = 25
SECTION_MAX_LINKS = 12

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
markdown_manager = Markdown(app)
asset_manager = AssetManager(app)


def discover_urls():
    return [('page', dict(path=page.path)) for page in pages]


@app.route('/')
def index():
    return render_template('page.html', page=pages.get_or_404('homepage'))


@app.route('/<path:path>/')
def page(path):
    return render_template('page.html', page=pages.get_or_404(path))


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
    local("cp ./static/*.ico ./master/")
    local("cp ./static/*.txt ./master/")
    local("cp ./static/CNAME ./master/")
    print("Done.")


@command
def serve(server='127.0.0.1', port=5000, debug=DEBUG):
    """ Serves this site.
    """
    asset_manager.config['ASSETS_DEBUG'] = debug
    if debug:
        app.debug = True
    app.run(host=server, port=port, debug=debug)


@command
def deploy(commit_message):
    """ Deploys this site to github pages.
    """
    build()
    build()
    print('Deploying website from %s to github...' % ROOT_DIR)
    os.chdir(os.path.join(ROOT_DIR, FREEZER_DESTINATION))
    local('git commit -a -m"%s"' % commit_message)
    print('Pushing to master branch')
    local('git push')
    os.chdir(ROOT_DIR)
    local('pwd')
    local('git add %s' % FREEZER_DESTINATION)
    local('git commit -a -m"%s"' % commit_message)
    print('Pushing to sources branch')
    local('git push')
    print('New version has been commited, pushed & deployed to github.')


if __name__ == '__main__':
    freezer.register_generator(discover_urls)
    parser = ArghParser()
    parser.add_commands([build, serve, deploy, ])
    parser.dispatch()
