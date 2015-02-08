#python
from flask import Flask, jsonify, json, request, render_template
import os
import jinja2
from flask.ext.assets import Environment, Bundle

app = Flask(__name__, static_url_path='')

assets = Environment(app)
js = Bundle('jquery.js', 'base.js', 'widgets.js',
            filters='jsmin', output='gen/packed.js')
assets.register('js_all', js)
# app.jinja_loader = jinja2.FileSystemLoader('app/templates') 

@app.route("/QuestionSets/Dolphin.json", methods=["GET", "POST"])
def questions():
    if request.method == "POST":
       SITE_ROOT = os.path.realpath(os.path.dirname('Dolfin'))
       json_url = os.path.join(SITE_ROOT, "QuestionSets", "Dolphin.json")
       data = json.load(open(json_url))
       return jsonify(data)

@app.route("/")
def home():
   return render_template("index.html")

@app.route("/signup.html")
def signup():
	return render_template("signup.html")

@app.route("/login.html")
def login():
	return render_template("login.html")

@app.route("/topics.html")
def topics():
	return render_template("topics.html")

@app.route("/about.html")
def about():
	return render_template("about.html")

@app.route("/dolphin-info.html")
def dolphin_info():
        return render_template("dolphin-info.html")

@app.route("/questionset.html")
def question():
        return render_template("questionset.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)


