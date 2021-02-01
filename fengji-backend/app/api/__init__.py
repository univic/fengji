
from app.api import user


def register_blueprint(app):
    app.register_blueprint(user.bp)
