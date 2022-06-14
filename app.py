from distutils.log import debug
from flask import *
from model.marugame import selection

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    if request.method == "POST":
        budget = request.form["budget"]
        udon, s_result, sum = selection(budget)

        if len(udon) == 0 and len(s_result) == 0:
            return render_template("failure.html")
        else:
            return render_template("result.html", udon=udon, s_result=s_result, sum=sum)

if __name__ == '__main__':
    app.run()