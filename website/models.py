from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import event
import json
import os

class MenuItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    alergens = db.Column(db.String(150))
    description = db.Column(db.String(350))
    price = db.Column(db.String(150))

@event.listens_for(MenuItems.__table__, 'after_create')
def create_MenuItems(*args, **kwargs):
    filepath = "{0}/website/Resources/MenuItems.json".format(os.getcwd())
    filepath = filepath.replace("\\", "/")
    with open(filepath) as f:
        data = json.load(f)
    for item in data["items"]:
        tempItem = MenuItems(id=item["id"], name = item["name"], alergens=item["alergens"], description = item["description"], price= item["price"])
        db.session.add(tempItem)
    db.session.commit()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))