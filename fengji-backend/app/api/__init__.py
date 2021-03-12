
from app.api import user, accounts, item, item_tag, report_group, group_role


def register_blueprint(app):
    app.register_blueprint(user.bp)
    app.register_blueprint(item.bp)
    app.register_blueprint(item_tag.bp)
    app.register_blueprint(report_group.bp)
    app.register_blueprint(group_role.bp)
