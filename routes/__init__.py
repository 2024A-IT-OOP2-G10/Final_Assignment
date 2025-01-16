from .lecture import lecture_bp
from .user import user_bp
from .absence import absence_bp
from .home import home_bp
from .absence import absence_bp

# Blueprintをリストとしてまとめる
blueprints = [user_bp, absence_bp, home_bp]
