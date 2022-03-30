from bottle import route, run

@route("/")
def index():
    return "Hello World!"

run(host="localhost", port=8080, debug=True)
# stranku lze v prohlizeci otevrit na adrese localhost:8080/
