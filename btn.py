from bottle import route, run

@route("/")
def index():
    return "<button>Klikni!</button>"

run()