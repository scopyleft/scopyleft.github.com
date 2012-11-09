#!/usr/bin/env python

from argh import *
from fabric.api import local
from flask import Flask, render_template, abort
from flask_frozen import Freezer
from flaskext.flatpages import FlatPages
from flaskext.markdown import Markdown
from flaskext.assets import Environment as AssetManager

# Configuration
DEBUG = False
BASE_URL = 'https://scopyleft.fr'
ASSETS_DEBUG = DEBUG
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'pages'
FREEZER_DESTINATION = 'master'

# App configuration
FEED_MAX_LINKS = 25
SECTION_MAX_LINKS = 12

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
markdown_manager = Markdown(app)
asset_manager = AssetManager(app)


@app.route('/')
def index():
    try:
        page = filter(lambda p: p.path == 'homepage', pages)[0]
    except:
        abort(404)
    return render_template('page.html', page=page)


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


if __name__ == '__main__':
    parser = ArghParser()
    parser.add_commands([build, serve, ])
    parser.dispatch()
