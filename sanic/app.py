from sanic import Sanic
from sanic.response import json

app = Sanic("Sanic Application")

@app.route('/')
async def test(request):
    return json({ 'message': 'Hello world from Sanic' })

if __name__ == '__main__':
    # Listen on all interfaces 
    # Used in conjunction with Gunicorn
    # https://sanicframework.org/en/guide/deployment/running.html
    app.run(host='0.0.0.0', port='8000')
