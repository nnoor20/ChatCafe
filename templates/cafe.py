from flask import Flask, render_template, request

app = Flask(__name__)

menu = {
    "coffee": {"price": 2.99, "description": "Freshly brewed coffee"},
    "latte": {"price": 3.99, "description": "Espresso with steamed milk and a layer of foam"},
    "cappuccino": {"price": 3.49, "description": "Espresso with steamed milk and more foam than a latte"},
    "croissant": {"price": 2.49, "description": "Flaky pastry with buttery flavor"},
    "bagel": {"price": 1.99, "description": "Soft and chewy, great with cream cheese or jam"},
    "muffin": {"price": 2.99, "description": "Freshly baked, great for breakfast or snack"}
}

@app.route('/')
def index():
    return render_template('welcome.html', menu=menu)


@app.route('/order', methods=['GET', 'POST'])
def order():
    message = ''
    if request.method == 'POST':
        items = request.form.getlist('items')
        total_price = sum([menu[item]['price'] for item in items])
        message = f'Thank you, {request.form["name"]} ({request.form["student_id"]})! Your order has been placed. Your total is ${total_price:.2f}.'
    return render_template('order.html', menu=menu, message=message)

if __name__ == '__main__':
    app.run(debug=True)

