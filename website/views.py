from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import MenuItems
from . import db
import json


views = Blueprint('views', __name__)
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        GF = request.form.get('GF')
        SF = request.form.get('SF')
        LI = request.form.get('LI') 
        if GF == None and SF == None and LI == None:
            MI = MenuItems.query.all()
        else:
            if GF:
                MI = MenuItems.query.filter(MenuItems.alergens.contains(GF))
            if SF:
                MI = MenuItems.query.filter(MenuItems.alergens.contains(SF))
            if LI:
                MI = MenuItems.query.filter(MenuItems.alergens.contains(LI))
    else:
        MI = MenuItems.query.all()
        GF = None
        SF = None
        LI = None

    return render_template("home.html", user=current_user, menuItems=MI, GF=GF, SF=SF, LI=LI)
