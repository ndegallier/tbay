from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, Float, ForeignKey, MetaData, func, desc


engine = create_engine('postgresql://ubuntu:football12@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()



class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    bids = relationship("Bid", backref="item")
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False) 
    
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    item = relationship("Item", backref="owner")
    bid = relationship("Bid", uselist=False, backref="bidder")
    


class Bid(Base):
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float(20,3), nullable=False)
    bid_time = Column(DateTime, default=datetime.utcnow)
    
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    bidder_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    
Base.metadata.create_all(engine)
m=MetaData()
m.reflect(engine)


# users 
Nick = User(username="nick", password="sports")
James = User(username="james", password="rice")
Nathan = User(username="nate", password="fries")

# item
Baseball = Item(name="baseball", owner=Nick)

# bids
natebid = Bid(price=12.58, bidder=Nathan, item=Baseball)
jamesbid = Bid(price=12.59, bidder=James, item=Baseball)

session.add_all([Nick, James, Nathan, Baseball, natebid, jamesbid])
session.commit()

highest_bidder= session.query(Bid).order_by(desc(Bid.price)).first()
print(highest_bidder.bidder.username)