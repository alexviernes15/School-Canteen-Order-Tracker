@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    for order in orders:
        if order["id"] == order_id:
            return jsonify(order), 200

    return jsonify({"error": "Order not found"}), 404
