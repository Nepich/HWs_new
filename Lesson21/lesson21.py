from flask import Flask

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


app.run(debug=True)
