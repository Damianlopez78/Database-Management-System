from flask import Flask
from flask import request
from flask import render_template
#import stringComparison

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['fullname']
    text2 = request.form['email']
    #plagiarismPercent = stringComparison.extremelySimplePlagiarismChecker(text1,text2)


if __name__ == '__main__':
    app.run(host="http://localhost:63342/project/index.html")