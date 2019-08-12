from flask import Flask, render_template, request, redirect, url_for, make_response
from models import User, db

app = Flask(__name__)
db.create_all()  #  0) DATENBANKTABELLEN WERDEN ERSCHAFFEN <=> CREATE

@app.route( "/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        name = request.form.get("name")
        mail = request.form.get("mail")
        songtitle = request.form.get("songtitle")

        print(name)
        print(mail)
        print(songtitle)

        user = User(name=name,
                    email=mail,
                    songtitle=songtitle)  # 2) DAS OBJEKT user WIRD MIT DEN WERTEN ERSTELLT, DIE IN DAS FORMULAR EINGEGEBEN WURDEN

        # save the user object into a database
        db.add(user)  # 3) DAS OBJEKT user WIRD IN DIE DATENBANK EINGEFÜGT <=> UPDATE
        db.commit()  # 4) AUSFÜHRUNG DER DATENBANKOPERATION

        response = make_response(redirect(url_for('success')))
        response.set_cookie("mail", mail)

        return response

@app.route("/impressum.html")
def impressum():
    return render_template("impressum.html", address = "Elmo the Red Monster, Sesamestreet 4, 12345 Monstertown")

@app.route("/success.html")
def success():
    return render_template("success.html", address = "Elmo the Red Monster, Sesamestreet 4, 12345 Monstertown")

if __name__ == '__main__':
    app.run()