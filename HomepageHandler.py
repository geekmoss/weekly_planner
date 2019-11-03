from BaseHandler import BaseHandler
import tornado.web


class HomepageHandler(BaseHandler):
    @tornado.web.addslash
    def get(self):
        self.render("homepage.html")
        pass
    pass
