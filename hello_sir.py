from bottle import route, run

@route("/")
@route("/<name>")
def index(name="Sir"):
    return f"Hello {name.title()}!"

run(debug=True)