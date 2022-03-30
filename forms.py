from bottle import route, run, request, template

@route("/form")
def form():
    return template("base.tpl", title="form", base="""
        <form action="/results" method="post">
            Jméno: <input type="text" name="jmeno">
            Příjmení: <input type="text" name="prijmeni">
            <input type="submit">
        </form>
    """)
    
@route("/results", method="POST")
def results():
    jmeno = request.forms.get("jmeno")
    prijmeni = request.forms.get("prijmeni")
    return template("results.tpl", jmeno=jmeno, prijmeni=prijmeni)

run()