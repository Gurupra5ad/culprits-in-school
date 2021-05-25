from flask import Flask, render_template, request, url_for, redirect, make_response, jsonify, json
from flask_mail import Mail, Message
from flask_mongoengine import MongoEngine


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)