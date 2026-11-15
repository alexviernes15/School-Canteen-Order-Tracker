from flask import Flask, jsonify, request

app = Flask(__name__)


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


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    for order in orders:
        if order["id"] == order_id:
            return jsonify(order), 200

    return jsonify({"error": "Order not found"}), 404


@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON body required"}), 400

    required = ["student_name", "items", "total_price"]

    if any(field not in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    if (not isinstance(data["student_name"], str)
            or not data["student_name"].strip()
            or not isinstance(data["items"], list)
            or not data["items"]
            or not all(isinstance(item, str) and item.strip()
                       for item in data["items"])
            or isinstance(data["total_price"], bool)
            or not isinstance(data["total_price"], (int, float))
            or data["total_price"] < 0):
        return jsonify({"error": "Invalid order information"}), 400

    new_order = {
        "id": max([o["id"] for o in orders], default=0) + 1,
        "student_name": data["student_name"].strip(),
        "items": data["items"],
        "total_price": data["total_price"],
        "status": "Pending"
    }

    orders.append(new_order)

    return jsonify({
        "message": "Order created successfully",
        "order": new_order
    }), 201


@app.route('/orders/<int:order_id>', methods=['PATCH'])
def update_order(order_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON body required"}), 400

    if "status" not in data:
        return jsonify({"error": "Status is required"}), 400

    allowed_statuses = [
        "Pending", "Preparing", "Ready", "Completed"
    ]

    if data["status"] not in allowed_statuses:
        return jsonify({"error": "Invalid order status"}), 400

    for order in orders:
        if order["id"] == order_id:
            order["status"] = data["status"]
            return jsonify({
                "message": "Order status updated",
                "order": order
            }), 200

    return jsonify({"error": "Order not found"}), 404


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    for order in orders:
        if order["id"] == order_id:
            orders.remove(order)
            return jsonify({
                "message": "Order deleted successfully"
            }), 200

    return jsonify({"error": "Order not found"}), 404

if __name__ == '_main_':
    app.run(debug=True)