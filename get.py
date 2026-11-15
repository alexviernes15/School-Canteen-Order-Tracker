From flask import Flask, jsonify

App = Flask(__name__)

Orders = [
    {
        “id”: 1,
        “student_name”: “John”,
        “items”: [“Burger”, “Juice”],
        “total_price”: 85,
        “status”: “Pending”
    }
]

@app.route(‘/orders’, methods=[‘GET’])
Def get_orders():
    Return jsonify({“orders”: orders}), 200

If __name__ == ‘__main__’:
    App.run(debug=True)

    