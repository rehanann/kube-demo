from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api =   Api(app)

@app.route("/")
def hello():
    return "Hello World!-v2"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
