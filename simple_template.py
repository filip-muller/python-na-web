from bottle import route, run, template

@route("/")
@route("/<jmeno>")
def index(jmeno="neznámé"):
    return template("Zadané jméno je {{jmeno}}", jmeno=jmeno.title())

run()