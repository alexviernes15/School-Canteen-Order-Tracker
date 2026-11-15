
orders = [
    {
        "id": 1,
        "student_name": "John",
        "items": ["Burger", "Juice"],
        "total_price": 85,
        "status": "Pending"
    }
]

def get_next_id():
    if not orders:
        return 1

    return max(order["id"] for order in orders) + 1
