#!/usr/bin/env python
from os.path import join, dirname
import click

# Tornado Imports
import tornado.httpserver
import tornado.ioloop
import tornado.web

from BaseHandler import NotFoundHandler
from HomepageHandler import HomepageHandler


class Application(tornado.web.Application):
    def __init__(self, debug):

        settings = {
            'debug': debug,
            'cookie_secret': "test",  # TODO: Fill this
            'static_path': join(dirname(__file__), 'static'),
            'template_path': join(dirname(__file__), 'templates'),
            # 'ui_methods': None,
        }

        handlers = [
            (r'/', HomepageHandler),
            (r'/.*', NotFoundHandler)
        ]

        tornado.web.Application.__init__(self, handlers, **settings)
        pass


@click.command()
@click.option('--port', '-p', default=5000, type=click.INT, help="Number of port")
@click.option('--address', '-a', type=click.STRING, help="Bind a interface")
@click.option('--debug', '-d', is_flag=True, help="Run server & app with debug mode")
def main(port, address, debug):
    app = Application(debug)

    if debug:
        app.listen(port, address)
        tornado.ioloop.IOLoop.instance().start()
        pass
    else:
        server = tornado.httpserver.HTTPServer(app)
        server.bind(port)
        server.start(2)
        tornado.ioloop.IOLoop.current().start()
        pass
    pass


if __name__ == '__main__':
    main()
    pass
