import os, random
from flask import Flask, Response
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__)

env = Environment(
    loader=PackageLoader("app"),
    autoescape=select_autoescape()
)

@app.route("/")
def hello():
    template = env.get_template("base.html")
    return Response(template.render(the="variables", go="here"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, use_reloader=True)

