from quart import Quart

app = Quart(__name__)

@app.route("/")
async def hello():
    return {"message": "Hello World, from Quart"}

@app.route("/api")
async def json():
    return {"message": "Hello from an API route"}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
