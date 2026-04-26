from mako.lookup import exceptions


def render(req, template, data):
    app = req.application
    data.update(app.template_globals)
    t = app.lookup.get_template(template)
    req.response.contenttype = 'text/html'

    data['req'] = req
    data['identity'] = req.identity if hasattr(req, 'identity') \
        else None
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
