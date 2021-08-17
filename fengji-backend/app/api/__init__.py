
from app.api import user, accounts, todo_item, tag_template, report_group, group_role, tag_template_group


def register_blueprint(app):
    app.register_blueprint(user.bp)
    app.register_blueprint(todo_item.bp)
    app.register_blueprint(tag_template.bp)
    app.register_blueprint(report_group.bp)
    app.register_blueprint(group_role.bp)
    app.register_blueprint(tag_template_group.bp)
