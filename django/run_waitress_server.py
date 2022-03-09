import os

from waitress import serve

from PythonDjangoWindows.wsgi import application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosql.settings") 

serve(application, host="0.0.0.0", port=os.environ["PORT"], url_scheme="https") 
