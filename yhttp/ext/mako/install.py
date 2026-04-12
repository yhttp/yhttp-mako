from mako.lookup import TemplateLookup

from .decorator import decoratorfactory


DEFAULT_SETTINGS = '''
modules: makomodules
cache:
  size: 500
lookup: templates
'''


def install(app, data=None):
    app.template = decoratorfactory
    app.settings.merge('mako: {}')
    app.settings['mako'].merge(DEFAULT_SETTINGS)
    app.template_globals = data if data else {}

    @app.when
    def ready(app):
        app.lookup = TemplateLookup(
            directories=app.settings.mako.lookup,
            module_directory=app.settings.mako.modules,
            collection_size=app.settings.mako.cache.size,
            filesystem_checks=app.settings.debug,
            output_encoding='utf-8',
        )
