from tg import expose, TGController, MinimalApplicationConfigurator
from wsgiref.simple_server import make_server


class RootController(TGController):
    @expose()
    def index(self):
        return 'Hello World, from TurboGears2'

    @expose()
    def hello(self, person):
        return 'Hello %s' % person


config = MinimalApplicationConfigurator()
config.update_blueprint({
    'root_controller': RootController()
})

application = config.make_wsgi_app()

print("Serving on port 8000...")
httpd = make_server('', 8000, application)
httpd.serve_forever()