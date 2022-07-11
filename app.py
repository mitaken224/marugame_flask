from distutils.log import debug
from flask import *
from model.marugame import selection

app = Flask(__name__)


@app.route("/")
def index():
    # 予算入力画面
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    if request.method == "POST":
        # 予算を受け取り、メニューを選ぶ関数selectionに渡す
        budget = request.form["budget"]
        udon, s_result, sum = selection(budget)

        # うどんもサイドメニューも頼めなければエラー画面
        if len(udon) == 0 and len(s_result) == 0:
            return render_template("failure.html")
        # 何か1つでも注文できれば結果表示画面
        else:
            return render_template("result.html", udon=udon, s_result=s_result, sum=sum)

if __name__ == '__main__':
    app.run()