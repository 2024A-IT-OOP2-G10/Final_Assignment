# Blueprintの作成
from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__, url_prefix='/home')

@home_bp.route('/')
def index():
    return render_template('home.html')