from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}>"


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        task_content = request.form['content']  # перемюб куда мы будем сохр-ть данные( ключ 'content' из index.html
        new_task = Todo(content=task_content)  # новая перюб кот будет экзю класса, именнованная перю content - это то,
                                                    # что введёт пользователь в поле content класса Тодо
        try:
            db.session.add(new_task)
            db.session.commit()  # данные записаллись в бд
            return redirect('/')
        except Exception as e:
            return f"Не удалось добавить вашу задачу {e}"
    else:          # иначе - отрабатывает GET
        tasks = Todo.query.order_by(Todo.date_created).all()  # достаём эти данные из базы, делаем сортировку
        # по дате создания
        return render_template('index.html', tasks=tasks)  # и передаём эту переменую на страничку html чезез имя tasks


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)  #Получить данные или вернуть страницу 404

    try:
        db.session.delete(task_to_delete) # удаляем методом delete из бд
        db.session.commit()  #и фиксируем данные в таком состоянии
        return redirect("/")
    except Exception as e:
        return f" Не удалось удалить задачу {e}"


@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form['content']  # Переменной взятой из базы из поля content присваеваем введённое
                                                # значение в форме ввода

        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f" Не удалось удалить задачу {e}"

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
