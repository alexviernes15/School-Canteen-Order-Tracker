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