from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello"


if __name__ == "__main__":
    print("Starting Python Flask Server for Testing")
    app.run()
