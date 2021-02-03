
from app.api import user
from app.api import accounts


def register_blueprint(app):
    app.register_blueprint(user.bp)
    app.register_blueprint(accounts.bp)
