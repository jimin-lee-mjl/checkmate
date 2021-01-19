from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def index():
  return render_template('home.html')

@app.route('/calendar')
def calendar():
    return render_template("calendar.html")

@app.route('/data')
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')

    with open("events.json", "r") as input_data:
        return input_data.read()
# @app.route('/calendar')
# def hello():
#     return render_template("/calendar/calendar.html")


if __name__=="__main__":
  app.run(debug=True)
