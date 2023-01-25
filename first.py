import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort


DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'd60e1f3b1e5ef48d86113c9cd0d6e9909c25b3a6'

app = Flask(__name__)
app.config.from_object(__name__)


app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))  # присоединение БД к корневому каталогу


# для соединения с базой данных
def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


# ф. для создания таблиц в БД
def create_db():
    db = connect_db()         # открыли БД
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()               # СОХРАНИЛИ БД
    db.close()                # закрыли БД

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Обратная связь", "url": "contact"},
]


@app.route("/index")
@app.route("/")
def index():
    print(url_for("index"))
    return render_template("index.html", title="Главная", menu=menu)


@app.route("/about")
def about():
    print(url_for("about"))
    return render_template("about.html", title="О нас", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"Пользователь: {username}"


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено успешно!', category='success')
        else:
            flash('Ошибка отправки', category='error')

    #     print(request.form)
    #     context = {
    #         'username': request.form['username'],
    #         'email': request.form['email'],
    #         'message': request.form['message']
    #     }
    #     return render_template("contact.html", **context, title="Обратная связь", menu=menu)

    return render_template("contact.html", title="Обратная связь", menu=menu)


@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'dmitry' and request.form['passw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template("login.html", title="Авторизация", menu=menu)

#
@app.errorhandler(404)  # ОБРАБОТЧИК СОБЫТИЙ ОШИБОК
def page_not_found(error):
    return render_template("page404.html", title="Страница не найдена", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
