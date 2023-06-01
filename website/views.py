from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
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
        flash('Filtering by: {0}, {1}, {2}'.format(GF,SF,LI), category='success')
    return render_template("home.html", user=current_user)
