from server.app import app, db
from server.models import Restaurant, Pizza, RestaurantPizza

with app.app_context():
    print(" Seeding data...")

    
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    
    r1 = Restaurant(name="Mario's Pizza", address="123 Tomato Lane")
    r2 = Restaurant(name="Luigi's Slice", address="456 Cheese St")
    
   
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")

   
    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=15, restaurant=r1, pizza=p2)
    rp3 = RestaurantPizza(price=8, restaurant=r2, pizza=p1)

    
    db.session.add_all([r1, r2, p1, p2, rp1, rp2, rp3])
    db.session.commit()

    print("Seeding complete!")
