from flask import Blueprint, jsonify, request
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.app import db

restaurant_pizza_bp = Blueprint('restaurant_pizza', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(rp)
        db.session.commit()
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    
    return jsonify({
        'id': rp.id,
        'price': rp.price,
        'restaurant_id': rp.restaurant_id,
        'pizza_id': rp.pizza_id,
        'pizza': {
            'id': rp.pizza.id,
            'name': rp.pizza.name,
            'ingredients': rp.pizza.ingredients
        },
        'restaurant': {
            'id': rp.restaurant.id,
            'name': rp.restaurant.name,
            'address': rp.restaurant.address
        }
    }), 201
    
