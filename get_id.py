
from flask import Blueprint, jsonify
from data import orders

get_order_bp = Blueprint("get_order", __name__)

@get_order_bp.route("/api/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    for order in orders:
        if order["id"] == order_id:
            return jsonify(order), 200

    return jsonify({"error": "Order not found"}), 404
