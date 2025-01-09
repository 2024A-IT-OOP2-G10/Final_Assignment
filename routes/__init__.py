from .lecture import lecture_bp
from .id import id_bp
from .home import home_bp

# Blueprintをリストとしてまとめる
blueprints = [id_bp, home_bp, lecture_bp]
