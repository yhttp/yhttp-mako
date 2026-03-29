import functools

from mako.lookup import TemplateLookup, exceptions


DEFAULT_SETTINGS = '''
modules: makomodules
cache:
  size: 500
lookup: templates
'''


def decoratorfactory(template, data=None):
    def decorator(handler):
        @functools.wraps(handler)
        def wrapper(req, *a, **kw):
            data = handler(req, *a, **kw)
            app = req.application
            data.update(app.template_globals)
            t = app.lookup.get_template(template)
            req.response.type = 'text/html'

            if hasattr(req, 'translator'):
                data['_'] = req.translator.gettext
                data['N_'] = req.translator.ngettext
                data['P_'] = req.translator.pgettext
                data['NP_'] = req.translator.pgettext
                data['l'] = req.locale

            try:
                return t.render(**data)
            except:  # noqa: E722
                return exceptions.html_error_template().render()

        return wrapper
    return decorator


def install(app, data=None):
    app.template = decoratorfactory
    app.settings.merge('mako: {}')
    app.settings['mako'].merge(DEFAULT_SETTINGS)
    app.template = decoratorfactory
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
