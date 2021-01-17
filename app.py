from flask import Flask, render_template

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
  return render_template('home.html')

@app.route('/calendar')
def hello():
    return render_template("calendar.html")


if __name__=="__main__":
  app.run(debug=True)