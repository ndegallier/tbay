# One-to-Many relationships in SQL

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    id = Column(Integer, primar_key=True)
    name = Column(String, nullable=False)
    guitars = relationship("Guitar", backref="manufacturer")
    
class Guitar(Base):
    __tablename__ = 'guitar'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'), nullable=False)

fender = Manufacturer(name="Fender")
strat = Guitar(name="Stratocaster", manufacturer=fender)
tele = Guitar(name="Telecaster")
fender.guitars.append(tele)


for guitar in fender.guitars:
    print(guitar.name)
print(tele.manufacturer.name)