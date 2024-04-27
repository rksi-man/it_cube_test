from flask import Flask, render_template
import random

app = Flask(__name__)



@app.route("/")
def hello_world():
    rand_nums = []
    for i in range(10):
        rand_nums.append(random.randint(0,100))
    return render_template("index.html", a=rand_nums)
