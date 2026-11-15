
from flask import Flask

from get import get_orders_bp
from get_id import get_order_id_bp
from post import create_order_bp
from Patch import update_order_bp
from Delete import delete_order_bp

app = Flask(__name__)

# Register all endpoints
app.register_blueprint(get_orders_bp)
app.register_blueprint(get_order_id_bp)
app.register_blueprint(create_order_bp)
app.register_blueprint(update_order_bp)
app.register_blueprint(delete_order_bp)

@app.route("/")
def home():
    return {
        "message": "School Canteen Order Tracker API",
        "status": "Running"
    }

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
