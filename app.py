import os, random
from flask import Flask, Response
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__)

env = Environment(
    loader=PackageLoader("app"),
    autoescape=select_autoescape()
)

USER = dict(
    callsign="G3VEK",
)

SYSTEM = dict(
    hostname="py-star",
)

SOFTWARE = dict(
    version="0.1.0",
    dashdate="20230522",
)

@app.route("/")
def hello():
    template = env.get_template("base.html")
    return Response(template.render(user=USER, system=SYSTEM, software=SOFTWARE))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, use_reloader=True)

