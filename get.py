from flask import Flask, jsonify, request

app = Flask(name)

Temporary order storage

orders = [
{
"id": 1,
"student_name": "John",
"items": ["Burger", "Juice"],
"total_price": 85,
"status": "Pending"
}
]

1. GET ALL ORDERS

@app.route('/orders', methods=['GET'])
def get_orders():
return jsonify({"orders": orders}), 200