from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', current_title = "INDEX PAGE")


@app.route('/about')
def fun1():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug = True)
