import random
import string

import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "Hello World, from CherryPy"

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
    cherrypy.config.update({ 
        'environment': 'production',
        'server.socket_host': '0.0.0.0', 
        'server.socket_port': 8000 
    })
    cherrypy.quickstart(StringGenerator())
