# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def add_op():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a, b))

@app.route('/sub')
def sub_op():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a, b))

@app.route('/mult')
def mult_op():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a, b))

@app.route('/div')
def div_op():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a, b))


operations = {
    "add": add, 
    "sub": sub, 
    "mult": mult, 
    "div": div
}

@app.route("/math/<operation>")
def math_time(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operations[operation](a, b))