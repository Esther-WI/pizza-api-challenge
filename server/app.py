from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2010@localhost:5432/pizza_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from server.models import Restaurant, Pizza, RestaurantPizza

    from server.controllers.restaurant_controller import restaurants_bp
    from server.controllers.pizza_controller import pizzas_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp
  
    app.register_blueprint(restaurants_bp)
    app.register_blueprint(pizzas_bp)
    app.register_blueprint(restaurant_pizza_bp)



    return app

app = create_app()