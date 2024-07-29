from flask import Flask
from views.user_view import user_blueprint
from views.order_view import order_blueprint

app = Flask(__name__)

# Registro de Blueprints
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(order_blueprint, url_prefix="/orders")

if __name__ == "__main__":
    app.run(debug=True)
