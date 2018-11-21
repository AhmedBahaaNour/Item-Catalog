from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.

session = DBSession()

# Create admin user
User1 = User(name="admin", email="ahmed.bahaa.nour@gmail.com")
session.add(User1)
session.commit()

# Menu for Pizza Hut 
restaurant1 = Restaurant(name="Pizza Hut", user_id="1")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Pan Pizza",
                     description=("is a thin or thick pizza" 
                      "baked in a deep dish pan."
                      "The bottoms"
                      "and sides of the crust become fried"
                      "and crispy in the oil used to coat the pan"),
                     price="$8.49", restaurant=restaurant1, user_id=1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(name="TEXAS BBQ PULLED BEEF",
                     description=("Savoury Pulled Beef with roasted"
                      "onions and sweet cherry tomatoes on a San"
                      "Francisco (SFO) style dough."),
                     price="$15",  restaurant=restaurant1, user_id=1)

session.add(menuItem2)
session.commit()


menuItem3 = MenuItem(name="CALIFORNIA VEGGIE & CHIC",
                     description=("The good ol' Californian style of"
                      "wild mushrooms, roasted chicken, cherry"
                      "tomatoes and fresh spinach on the new"
                      "San Francisco (SFO) style dough."),
                     price="$5.50", restaurant=restaurant1, user_id=1)

session.add(menuItem3)
session.commit()


# Menu for Cinnabon
restaurant2 = Restaurant(name="Cinnabon")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Cinnabon Classic Roll",
                     description=("Warm dough filled with our"
                      "legendary Makara Cinnamon, topped with"
                      "rich cream cheese frosting."),
                     price="$3.79", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Caramel Pecanbon Roll",
                     description=("We've added a caramel twist"
                      "to our beloved Classic Roll. Layers of"
                      "our legendary Makara Cinnamon are wrapped"
                      "in warm dough and swirled with smooth"
                      "caramel frosting"),
                     price="$4.75",  restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Cinnabon Stix 10pc.",
                     description=("It's made with the chain's"
                     "signature dough, which is twisted, covered"
                     "with Cinnabon Makara cinnamon and sugar,"
                     "and freshly baked"),
                     price="$5.49", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

print "Added menu items!"