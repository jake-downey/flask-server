from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def root():
    return '<p>Hello, Jake!</p>'

@app.route("/blue")
def blue():
    return '<p style="color: blue;">Hello, Jake!</p>'

@app.route("/sum", methods=['GET'])
def sum_get():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    sum = x + y
    return str(sum)

@app.route("/sum", methods=['POST'])
def sum_post():
    data = request.form
    x = float(data.get('x'))
    y = float(data.get('y'))
    sum = x + y
    return str(sum)
