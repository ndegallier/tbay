# Many to Many relationships in SQL

from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

pizza_topping_table = Table('pizza_topping_association', Base.metadata, 
    Column('pizza_id', Integer, ForeignKey('pizza.id')), 
    Column('topping_id', Integer, ForeignKey('topping.id'))
    )

class Pizza(Base):
    __tablename__ = 'pizza'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    toppings = relationship("Topping", secondary="pizza_topping_association",
    backref="pizzas")

class Topping(Base):
    __tablename__ = 'topping'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
peppers = Topping(name="Peppers")
garlic = Topping(name="Garlice")
chilli = Topping(name="Chilli")

spicy_pepper = Pizza(name="Spicy Pepper")
    