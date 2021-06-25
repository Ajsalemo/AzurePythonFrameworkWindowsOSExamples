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
    # Tornado uses it's own HTTP server to start the application
    main()