from flask import Flask
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return "Первая страница на FLASK"


@app.route('/2')
def second_page():
    return 'Вторая страница на FLASK'


@app.route('/3')
def third_page():
    return 'Третья страница на FLASK и немного белеберды JK:HKLJBVJJK:BGHJKCFYJOLG'


@app.route('/DB/<int:pk>')
def from_db(pk):
    connection = sqlite3.connect("lesson22_db.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM data')
    data = cursor.fetchall()
    if pk > len(data):
        return 'Такого значения нет в базе данных'
    else:
        cursor.execute('SELECT * FROM data WHERE pk=?', (pk, ))
        data = cursor.fetchone()
        return f'Имя = {data[0]}, дата рождения: {data[1]}'


app.run(debug=True)
