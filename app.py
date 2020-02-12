from flask import Flask, render_template
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

app = Flask(__name__)
engine = create_engine("postgres://imperial:imperial-fdt-2019@imperial.ckp3dl3vzxoh.eu-west-2.rds.amazonaws.com:5432/dvdrental", echo = True)
Base = declarative_base()

class Country(Base):
    __tablename__ = 'country'
    country_id = Column(Integer, primary_key = True)
    country = Column(String)
    
    def __repr__(self):
        return self.country
    
Session = sessionmaker()
Session.configure(bind = engine)
session = Session()
countries = session.query(Country).all()

@app.route('/')
def hello_world():
    return render_template("index.html", len = len(countries), countries = countries)













