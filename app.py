from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Mahdi you completed phase 1 of this project!!!'
