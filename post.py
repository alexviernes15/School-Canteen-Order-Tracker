
from flask import Blueprint, jsonify, request
from data import orders, get_next_id

create_order_bp = Blueprint("create_order", __name__)

@create_order_bp.route("/api/orders", methods=["POST"])
def create_order():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    required_fields = ["student_name", "items", "total_price"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    if not isinstance(data["student_name"], str) or not data["student_name"].strip():
        return jsonify({"error": "Invalid student name"}), 400

    if not isinstance(data["items"], list) or not data["items"]:
        return jsonify({"error": "Items must be a non-empty list"}), 400

    if (
        isinstance(data["total_price"], bool)
        or not isinstance(data["total_price"], (int, float))
        or data["total_price"] < 0
    ):
        return jsonify({"error": "Invalid total price"}), 400

    new_order = {
        "id": get_next_id(),
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
