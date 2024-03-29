# -*- coding: utf-8 -*-
import os

from .app import create_app

try:
    from werkzeug.contrib.fixers import ProxyFix
except ModuleNotFoundError:
    # Werkzeug >1.0 moved the library to middleware : https://github.com/pallets/werkzeug/issues/1477
    from werkzeug.middleware.proxy_fix import ProxyFix


app = create_app(config_file=os.environ["SCOUT_CONFIG"])

app.wsgi_app = ProxyFix(app.wsgi_app)
