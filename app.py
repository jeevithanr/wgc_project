from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world"

@app.route("/jeevi")
def jeevi():
    return "hi jeevithan"

if __name__ == '__main__':
    app.run(debug=True)
