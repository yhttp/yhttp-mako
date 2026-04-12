import functools

from .handler import render


def decoratorfactory(template, data=None):
    def decorator(handler):
        @functools.wraps(handler)
        def wrapper(req, *a, **kw):
            data = handler(req, *a, **kw)
            return render(req, template, data)

        return wrapper
    return decorator
