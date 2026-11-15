
from flask import Blueprint, jsonify
from data import orders

get_orders_bp = Blueprint("get_orders", __name__)

@get_orders_bp.route("/api/orders", methods=["GET"])
def get_orders():
    return jsonify(orders), 200
