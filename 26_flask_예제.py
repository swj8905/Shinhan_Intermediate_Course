from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/test")
def test():
    return "Test!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")