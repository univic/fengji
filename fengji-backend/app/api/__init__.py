
from app.api import user, accounts, item, item_tag


def register_blueprint(app):
    app.register_blueprint(user.bp)
    app.register_blueprint(item.bp)
    app.register_blueprint(item_tag.bp)
