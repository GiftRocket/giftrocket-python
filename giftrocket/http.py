##############################################################################
# Helper module that encapsulates the HTTPS request so that it can be used
# with multiple runtimes. PK Mar. 14
##############################################################################
import os
import json

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

__version__ = '1.0.0'

ALLOWED_METHODS = {'delete', 'get', 'patch', 'post', 'put'}


def _requests(url, method, data):
    import requests

    normalized_method = method.lower()
    if normalized_method in ALLOWED_METHODS:
        return getattr(requests, normalized_method)(url, data=json.dumps(data), headers={
            'User-Agent': 'GiftRocket Python v{}'.format(__version__),
            'Content-type': 'application/json', 'Accept': 'text/plain'
        })
    else:
        raise ValueError(
            'Invalid request method {}'.format(method)
        )


# Google App Engine
def _urlfetch(url, method, data):
    from google.appengine.api import urlfetch

    method = method.upper()
    qs = urlencode(data)
    if method == 'POST':
        payload = qs
    else:
        payload = None
        url += '?' + qs

    headers = {
        'User-Agent': 'GiftRocket Python v{}'.format(__version__)
    }

    res = urlfetch.fetch(
        url,
        follow_redirects=True,
        method=method,
        payload=payload,
        headers=headers,
        deadline=60  # seconds
    )

    # Add consistent interface across requests library and urlfetch
    res.ok = res.status_code >= 200 and res.status_code < 300
    res.text = res.content
    return res


def to_requests(base_url, auth):
    # _is_appengine caches one time computation of os.environ.get().
    # Closure means that _is_appengine is not a file scope variable
    _is_appengine = os.environ.get('SERVER_SOFTWARE', '').split('/')[0] in (
        'Development',
        'Google App Engine',
    )

    req = _urlfetch if _is_appengine else _requests

    def inner(path, method, data=None):
        return req(
            "{}/{}".format(base_url, path),
            method,
            dict(data or {}, **auth)
        )
    return inner
