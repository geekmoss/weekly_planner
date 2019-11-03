from typing import Optional, Awaitable, Any
from http import HTTPStatus
import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def initialize(self) -> None:
        pass

    def prepare(self) -> Optional[Awaitable[None]]:
        return

    def on_finish(self) -> None:
        pass

    def write_error(self, status_code: int, **kwargs: Any) -> None:
        self.set_status(HTTPStatus.INTERNAL_SERVER_ERROR, 'Internal Server Error')
        self.render('static/500.html')
        return

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        return

    def not_found(self):
        self.set_status(HTTPStatus.NOT_FOUND, "Not Found")
        self.render('static/404.html')
        return

    def forbidden(self):
        self.set_status(HTTPStatus.FORBIDDEN, "Forbidden")
        self.render('static/403.html')
        return

    def get_current_user(self) -> Any:
        return None
    pass


class NotFoundHandler(BaseHandler):
    def get(self):
        self.not_found()
        return
    pass
