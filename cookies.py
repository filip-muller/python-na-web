from urllib import response
from bottle import route, run, request, response as response_

@route("/")
def index():
    if request.get_cookie("navstiveno"):
        return "Vítej zpět!"
    else:
        response_.set_cookie("navstiveno", "ano", max_age=600)
        return "Rádi tě poznáváme"
    
run()