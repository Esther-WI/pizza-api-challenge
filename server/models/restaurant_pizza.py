from server.app import db 


from sqlalchemy.orm import validates

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizza'
    __table_args__ = {'extend_existing': True}


    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable= False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    @validates('price')
    def validate_price(self, key, value):
        if value <1 or value > 30:
            raise ValueError('Price must be between 1 and 30')
        return value