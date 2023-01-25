# import os
#
# from sqlalchemy import and_, or_, not_, desc, func, distinct, text
#
# from mod.database import DATABASE_NAME, Session
# import create_database as db_creator
#
# from mod.author import Author, association_table
# from mod.person import Person
# from mod.group import Group
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()
#
#     session = Session()
#     print(session.query(Author).all())  # результат запроса по всем элементам в виде списка
#     print("*" * 60)


#     for it in session.query(Lesson):
#         print(it.lesson_title)
#     print("*" * 60)
# print(session.query(Lesson).count())  # количество записей в запросе
# print("*" * 60)
# print(session.query(Lesson).first())  # первый результат в запросе
# print("*" * 60)
# print(session.query(Lesson).get(3))  # результат по номеру первичного ключа
# print("*" * 60)
# for it in session.query(Lesson).filter(Lesson.id >= 3, Lesson.lesson_title.like('Ф%')):  # отфильтровать
#     # результаты по условию
#     print(it)
# print("*" * 60)
# for it in session.query(Lesson).filter(and_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
#     print(it)
# print("*" * 60)
# for it in session.query(Lesson).filter(or_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
#     print(it)
# print("*" * 60)
#
# for it, gr in session.query(Lesson.lesson_title, Group.group_name).filter(and_(association_table.c.lesson_id ==
# Lesson.id, association_table.c.group_id == Group.id, Group.group_name == 'MDA-9')):
#     print(it, gr)
# print("*" * 60)
#
# for it in session.query(Lesson).filter(not_(Lesson.id >= 3), not_(Lesson.lesson_title.like('Ф%'))):
#     print(it)
# print("*" * 60)
#
# print(session.query(Lesson).filter(Lesson.lesson_title is None).all())  # список записей в которых предметы не
# # определены
# print("*" * 60)
#
# print(session.query(Lesson).filter(Lesson.lesson_title is not None).all())  # список записей в которых предметы
# # определены
# print("*" * 60)
#
# print(session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Линейная алгебра'])).all())  # все
# # записи у которых названия предметов находятся в перечисленном списке
# print("*" * 60)
#
# print(session.query(Lesson).filter(Lesson.lesson_title.notin_(['Математика', 'Линейная алгебра'])).all())  # все
# # записи у которых названия предметов не находятся в перечисленном списке
# print("*" * 60)
#
# print(session.query(Student).filter(Student.age.between(16, 17)).all())  # студенты 16 и 17 лет
# print("*" * 60)
#
# print(session.query(Student).filter(not_(Student.age.between(17, 24))).all())  # студенты не находятся в диапазоне
# # 17 до 24 лет
# print("*" * 60)
#
# print(session.query(Student).filter(Student.age.like("1%")).all())  # соответствует заданному шаблону
# print("*" * 60)
#
# for it in session.query(Student).filter(Student.age.like("1%")).limit(4):  # количество записей для вывода
#     print(it)
# print("*" * 60)
#
# for it in session.query(Student).filter(Student.age.like("1%")).limit(4).offset(3):  # смещение элементов
#     print(it)
# print("*" * 60)
#
# for it in session.query(Student).order_by(Student.surname):  # сортировка по возрастанию
#     print(it)
# print("*" * 60)
#
# for it in session.query(Student).order_by(desc(Student.surname)):  # сортировка по убыванию
#     print(it)
# print("*" * 60)
#
# for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-7'):
#     print(it)
# print("*" * 60)
#
# for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name):
#     print(it)
# print("*" * 60)
#
# for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(
#         Group.group_name).having(func.count(Student.surname) < 25):
#     print(it)
# print("*" * 60)
#
# for it in session.query(distinct(Student.age)):
#     print(it)
# print("*" * 60)
#
# for it in session.query(Student.age).filter(Student.age < 20).distinct():
#     print(it)
# print("*" * 60)

# i = session.query(Lesson).get(7)
# i.lesson_title = "Информатика"
# session.add(i)
# session.commit()
#
# for it in session.query(Lesson):
#     print(it.lesson_title)
# print("*" * 60)

# session.query(Lesson).filter(
#     Lesson.lesson_title.like("%м%")
# ).update({"lesson_title": "M"}, synchronize_session="fetch")
# session.commit()

# for it in session.query(Lesson):
#     print(it.lesson_title)
# print("*" * 60)
#
# session.add(Lesson(lesson_title="Физика"))
# session.commit()

# for it in session.query(Lesson):
#     print(it.lesson_title)
# print("*" * 60)
#
# i = session.query(Lesson).filter(Lesson.lesson_title == "Физика").first()
# print(i)
# session.delete(i)
# session.commit()
#
# for it in session.query(Lesson):
#     print(it.lesson_title)
# print("*" * 60)

# for it in session.query(Student).filter(text("surname like 'В%'")).order_by(text("name, id desc")):
#     print(it)


# шаблонизатор

# pip install jinja2

# from jinja2 import Template


# name = "Игорь"
# age = 28
# per = {'name': "Игорь", 'age': 28}
#
# tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.name }}.")
# msg = tm.render(p=per)
#
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#
# per = Person("Игорь", 28)
#
# tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p.get_name() }}.")
# msg = tm.render(p=per)
#
# print(msg)

# data = """{% raw %}Модуль Jinja вместо
# определения {{ name }}
# подставит соответствующее значение {% endraw %}"""
#
# tm = Template(data)
# msg = tm.render(name="Игорь")
#
# print(msg)

#________________________________________________________
from jinja2 import Environment, FileSystemLoader

subs = ["Культура", "Наука", "Политика", "Спорт"]
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render(list_table=subs)

print(msg)



