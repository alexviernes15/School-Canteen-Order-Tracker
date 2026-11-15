
from flask import Blueprint, jsonify, request
from data import orders

update_order_bp = Blueprint("update_order", __name__)

@update_order_bp.route("/api/orders/<int:order_id>", methods=["PATCH"])
def update_order(order_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    if "status" not in data:
        return jsonify({"error": "Status is required"}), 400

    allowed_statuses = [
        "Pending",
        "Preparing",
        "Ready",
        "Completed"
    ]

    if data["status"] not in allowed_statuses:
        return jsonify({"error": "Invalid order status"}), 400

    for order in orders:
        if order["id"] == order_id:
            order["status"] = data["status"]

            return jsonify({
                "message": "Order updated successfully",
                "order": order
            }), 200

    return jsonify({"error": "Order not found"}), 404
