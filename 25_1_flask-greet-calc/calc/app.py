# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# @app.route('/add')
# def do_add():
#     """Add a and b"""

#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     return str(add(a, b))

# @app.route('/sub')
# def do_sub():
#     """Subtruct a and b"""
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     return str(sub(a, b))

# @app.route("/mult")
# def do_mult():
#     """Multiply a and b"""
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     return str(mult(a, b))

# @app.route("/div")
# def do_div():
#     """Divide a and b"""
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     return str(div(a, b))

operators = {
  "add": add,
  "sub": sub,
  "mult": mult,
  "div": div,
}

@app.route(/math/<opers>)
def do_math(opers):
    """Do math on a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[opers](a, b)

    return str(result)