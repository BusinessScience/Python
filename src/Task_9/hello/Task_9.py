from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
@app.route('/index')
def index():
    return render_template("index.html", name= 'coś')
@app.route('/form')
def form():
    return render_template("form.html")
@app.route('/result')
def result():
    name = request.args.get("name")
    surname = request.args.get("surname")
    age = request.args.get("age")
    return render_template("getResult.html", name=name, surname=surname, age=age)

if __name__ == '__main__':
    app.run(debug=True)