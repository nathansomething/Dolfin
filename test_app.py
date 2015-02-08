#python
from flask import Flask, jsonify, json, request, render_template
import os
import jinja2
SITE_ROOT = os.path.realpath(os.path.dirname('app'))
app = Flask(__name__)
# app.jinja_loader = jinja2.FileSystemLoader('app/templates') 

@app.route("/dolphins/questions")
def questions():
    json_url = os.path.join(SITE_ROOT, "templates/Dolfin/QuestionSets", "Dolphin.json")
    data = json.load(open(json_url))
    return jsonify(data)



@app.route("/")
def home():
   return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')


