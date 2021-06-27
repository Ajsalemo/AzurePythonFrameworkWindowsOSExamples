from tg import expose, TGController, MinimalApplicationConfigurator
from wsgiref.simple_server import make_server
import os

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

# Grab the local machines port exposed through the %HTTP_PLATFORM_PORT% variable which is passed in as %PORT% through we.config
platform_handler_port = int(os.environ.get('PORT'))
httpd = make_server('0.0.0.0', platform_handler_port, application)
httpd.serve_forever()