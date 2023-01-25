from flask import Flask, render_template, url_for

app = Flask(__name__)


menu = [
    {"name": "Продажа/ Покупка автомобилей", "url": "index"},
    {"name": "ПРОДАТЬ/ КУПИТЬ", "url": "sall"},
    {"name": "АВТОСАЛОНЫ", "url": "salons"},
    {"name": "АВТОСЕРВИСЫ", "url": "autoservis"},
]


@app.route("/index")
@app.route("/")
def index():
    print(url_for("index"))
    return render_template("/index.html", title="Продажа, покупка и сервис автомобилей", menu=menu)


@app.route("/sall")
def sall():
    print(url_for("sall"))
    return render_template("/sall.html", title="Продать/ Купить Автомобиль", menu=menu)


@app.route("/salons")
def salon():
    print(url_for("salon"))
    return render_template("/salons.html", title="Автосалоны", menu=menu)


@app.route("/autoservis")
def autoservis():
    print(url_for("autoservis"))
    return render_template("/autoservis.html", title="Автосервисы", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


if __name__ == "__main__":
    app.run(debug=True)
