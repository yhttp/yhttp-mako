import os

from bddrest import status, response

from yhttp.ext import mako, i18n


def test_extension(httpreq, app, mockupfs):
    tmpfs = mockupfs(**{
        'modules': {},
        'templates': {
            'index.mako': '${foo}'
        }
    })
    i18n.install(app)
    mako.install(app)
    app.settings.mako.lookup = f'{tmpfs}/templates'
    app.settings.mako.modules = f'{tmpfs}/modules'
    app.ready()

    @app.route()
    @app.i18n
    @app.template('index.mako')
    def get(req):
        return dict(foo='Foo')

    with httpreq():
        assert status == 200
        assert response == 'Foo'

    assert os.path.exists(f'{tmpfs}/modules/index.mako.py')


def test_render_error(httpreq, app, mockupfs):
    tmpfs = mockupfs(**{
        'modules': {},
        'templates': {
            'index.mako': '${notdefined}'
        }
    })
    mako.install(app)
    app.settings.mako.lookup = f'{tmpfs}/templates'
    app.settings.mako.modules = f'{tmpfs}/modules'
    app.ready()

    @app.route()
    @app.template('index.mako')
    def get(req):
        return dict(foo='Foo')

    with httpreq():
        assert status == 200
