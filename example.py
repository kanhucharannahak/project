
from flask import Flask,request
app = Flask(__name__)   # we are creating an instance

@app.route('/')   
def greet():
    return ("hello kanhu , samar is good student")


@app.route('/greet1')
def greet1():
    return("how are you samar")


@app.route('/greet2')
def greet2():
    return("samar gf name is urvasi")


@app.route('/addition')
def addition():
    a=10
    b=20
    return([a+b])

@app.route('/addition1')
def addition1():
    num1=request.args.get("num1")
    num2=request.args.get("num2")
    return([int(num1)+int(num2)])

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8000)