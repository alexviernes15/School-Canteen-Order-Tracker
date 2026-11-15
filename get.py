from flask import Flask, jsonify, request

app = Flask(name)


orders = [
{
"id": 1,
"student_name": "John",
"items": ["Burger", "Juice"],
"total_price": 85,
"status": "Pending"
}
]


@app.route('/orders', methods=['GET'])
def get_orders():
return jsonify({"orders": orders}), 200