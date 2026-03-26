import os

from bddrest import status, response
from yhttp.core import text

from yhttp.ext.mako import install


def test_extension(httpreq, app, tempdir):
    install(app)
    app.ready()

    @app.route()
    @app.template('index.mako')
    def get(req):
        return req.translator.gettext('foo')

    with httpreq():
        assert status == 200
        assert response == 'foo'
