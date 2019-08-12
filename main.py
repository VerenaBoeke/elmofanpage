from flask import Flask, render_template

app=Flask(__name__)#MODEL

@app.route("/")#CONTROLLER
def index():
    return render_template("index.html", address = "Elmo the Red Monster, Sesamestreet 4, 12345 Monstertown")

@app.route("/impressum.html")#CONTROLLER
def impressum():
    return render_template("impressum.html", address = "Elmo the Red Monster, Sesamestreet 4, 12345 Monstertown")

if __name__ == '__main__':
    app.run()