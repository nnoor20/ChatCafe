from flask import Flask, request, render_template

# Create app
app = Flask(__name__)

### Cafe

# Menu items
menu = {
    "coffee": {"price": 2.99, "description": "Freshly brewed coffee"},
    "latte": {"price": 3.99, "description": "Espresso with steamed milk and a layer of foam"},
    "cappuccino": {"price": 3.49, "description": "Espresso with steamed milk and more foam than a latte"},
    "croissant": {"price": 2.49, "description": "Flaky pastry with buttery flavor"},
    "bagel": {"price": 1.99, "description": "Soft and chewy, great with cream cheese or jam"},
    "muffin": {"price": 2.99, "description": "Freshly baked, great for breakfast or snack"}
}

# Welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html', menu=menu)


# Order page
@app.route('/order', methods=['GET', 'POST'])
def order():
    message = ''
    if request.method == 'POST':
        items = request.form.getlist('items')
        total_price = sum([menu[item]['price'] for item in items])
        message = f'Thank you for you order, {request.form["name"]} ({request.form["student_id"]})! Your order has been placed. Your total is ${total_price:.2f}.'
    return render_template('order.html', menu=menu, message=message)


### Chat

# List to store chat messages
messages = []

# Chat page 
@app.route('/chat', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('chat.html', username=username, messages=messages)
    return render_template('index.html')

# Send message
@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    username = request.form['username']
    messages.append((username, message))
    return render_template('chat.html', username=username, messages=messages)


# Run app
if __name__ == '__main__':
    app.run(debug=True)
