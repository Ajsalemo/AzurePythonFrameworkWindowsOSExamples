import os  
from waitress import serve  
import app

hug_app = app.__hug_wsgi__

serve(hug_app, host="0.0.0.0", port=os.environ["PORT"])
