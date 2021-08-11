from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route("/teacherlogin")
def teacherlogin():
    return render_template("teacherlogin.html")


@app.route("/studentlogin")
def studentlogin():
    return render_template("studentlogin.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")



if __name__ == '__main__':
    app.run(debug = True)