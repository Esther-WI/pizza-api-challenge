from server.app import db 


class Pizza(db.Model):
    __tablename__ = 'pizza'
    __table_args__ = {'extend_existing': True}


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza', cascade='all, delete-orphan')