from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Привет, мир!"

@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        return f'Результат: {result}'

    return '''
        <form method="post">
            Число 1: <input type="text" name="num1"><br>
            Число 2: <input type="text" name="num2"><br>
            <input type="submit" value="Сложить">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
