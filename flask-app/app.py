from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', current_title = "Custom Title111")


@app.route('/page1')
def fun1():
    
    pass


if __name__ == '__main__':
    app.run(debug = True)
