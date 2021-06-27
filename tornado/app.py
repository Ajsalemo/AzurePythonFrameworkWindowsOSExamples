import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world, from Tornado - deployed with Azure DevOps pipelines")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


def main():
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    # Tornado uses its own HTTP server
    app = make_app()
    # Grab the variable %PORT% which is passed in through web.config
    # %PORT%'s value is actually %HTTP_PLATFORM_PORT% - we can either pass this in directly or rename it as we're doing now
    # to successfully start a webserver, we need to listen on the target machines port
    http_platform_port = int(os.environ.get('PORT'))
    app.listen(http_platform_port)
    tornado.ioloop.IOLoop.current().start()
    main()