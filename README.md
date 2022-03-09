# AzurePythonFrameworkWindowsOSExamples

A repo housing multiple Python quickstart/"hello world" framework & libraries examples that are deployed on Azure in a Windows environment using IIS and HttpPlatformHandler along with Waitress being used as a production grade WSGI server. 

**Important**:
App Service creation for creation for Windows Python App Services can no longer be done in the portal. Creation can be done via the Azure CLI with the following command: `az webapp create -g "rgname" -p "appserviceplan" -n "appservicename" --runtime "PYTHON|3.6"`

<br>

- [Bottle](https://bottlepy.org/docs/dev/)
- [CherryPy](https://cherrypy.org/)
- [Dash](https://dash.plotly.com/introduction)
- [Falcon](https://falconframework.org/)
- [Hug](https://www.hug.rest/)
- [Tornado](https://www.tornadoweb.org/en/stable/)
- [TurboGears](https://turbogears.org/)
- [Web2Py](http://web2py.com/)
- [Django](https://www.djangoproject.com/)