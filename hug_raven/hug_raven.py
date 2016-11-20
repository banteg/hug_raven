from ipaddress import ip_address

import hug
from falcon import Request
from raven import Client
from raven.utils.wsgi import get_environ


class Sentry:
    def __init__(self, api: hug.API, client: Client = None, **kwargs):
        self.api = api
        self.client = Client(**kwargs) if client is None else client
        self.mount()

    def mount(self):
        hug.exception(api=self.api)(self.handle)

    def unmount(self):
        self.api.http.exception_handlers().pop(Exception)

    def handle(self, request, response, exception):
        self.capture(request, response, exception)
        return self.respond(request, response, exception)

    def capture(self, request, response, exception):
        data = self.context(request)
        self.client.captureException(exc_info=True, data=data)

    def respond(self, request, response, exception):
        raise exception

    def context(self, request: Request):
        return {
            'request': self.request_info(request),
            'user': self.user_info(request),
        }

    def request_info(self, request: Request):
        return {
            'url': request.url,
            'method': request.method,
            'query_string': request.query_string,
            'cookies': request.cookies,
            'headers': request.headers,
            'env': dict(get_environ(request.env)),
        }

    def user_info(self, request: Request):
        return {
            'id': None,
            'email': None,
            'username': request.context.get('user'),
            'ip_address': self.guess_ip(request),
        }

    def guess_ip(self, request: Request):
        for ip in request.access_route:
            try:
                ip_address(ip)
            except ValueError:
                pass
            else:
                return ip
