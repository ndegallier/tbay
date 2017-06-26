# One to one relationships in SQL

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationships

# Need to import more, as well as set up an engine

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    passport = relationship("Passport", uselist=False, backref="owner")

class Passport(Base):
    __tablename__ = 'passport'
    id = Column(Integer, primary_key=True)
    issue_date = Column(Date, nullable=False, default=datetime.utcnow)

# here is the one-to-one relationship, we reference person id. 
# the column we create below matches passport to owner
    
    owner_id = Column(Integer, ForeignKey('person.id'), nullable=False)

beyonce = Person(name="Beyonce Knowles")
passport = Passport()
beyonce.passport = passport

session.add(beyonce)
session.commit()

print(beyonce.passport.issue_date)
print(passport.owner.name)