from flask import Flask, request, render_template

app = Flask(__name__)

# List to store chat messages
messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('chat.html', username=username, messages=messages)
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    username = request.form['username']
    messages.append((username, message))
    return render_template('chat.html', username=username, messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
