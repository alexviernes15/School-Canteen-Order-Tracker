
from flask import Blueprint, jsonify
from data import orders

delete_order_bp = Blueprint("delete_order", __name__)

@delete_order_bp.route("/api/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    for order in orders:
        if order["id"] == order_id:
            orders.remove(order)

            return jsonify({
                "message": "Order deleted successfully"
            }), 200

    return jsonify({"error": "Order not found"}), 404
