from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route('/')
def homepage():
    time = datetime.datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return f"""
    <h1>Homepage.</h1>
    <p>It is currently {time}.</p>
    """

if __name__ == '__main__':
    app.run()
