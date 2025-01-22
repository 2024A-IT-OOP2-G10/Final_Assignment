from .lecture import lecture_bp
from .user import user_bp
from .absence import absence_bp
from .home import home_bp
from .lecture_result import lectureResult_bp
from .id import id_bp
from .todo import todos_bp

# Blueprintをリストとしてまとめる
blueprints = [user_bp, id_bp, home_bp, lecture_bp,lectureResult_bp,todos_bp]