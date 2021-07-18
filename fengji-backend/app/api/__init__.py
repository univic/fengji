
from app.api import user, accounts, item, tag_template, report_group, group_role, tag_group


def register_blueprint(app):
    app.register_blueprint(user.bp)
    app.register_blueprint(item.bp)
    app.register_blueprint(tag_template.bp)
    app.register_blueprint(report_group.bp)
    app.register_blueprint(group_role.bp)
    app.register_blueprint(tag_group.bp)
