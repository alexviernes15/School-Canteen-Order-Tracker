@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    for order in orders:
        if order["id"] == order_id:
            orders.remove(order)
            return jsonify({
                "message": "Order deleted successfully"
            }), 200

    return jsonify({"error": "Order not found"}), 404

if _name_ == '_main_':
    app.run(debug=True)