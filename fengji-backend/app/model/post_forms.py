# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-01-31

from wtforms import Form, BooleanField, StringField, validators, ValidationError
from app.config import app_config
import app.utilities.wtforms_validators as wtforms_validators


class RegistrationForm(Form):
    username = StringField('username',
                           [validators.InputRequired('未填写用户名'),
                            validators.Length(min=app_config.USER_SETTINGS['MIN_USERNAME_LENGTH'],
                                              max=app_config.USER_SETTINGS['MAX_USERNAME_LENGTH'],
                                              message=f"用户名长度需为{app_config.USER_SETTINGS['MIN_USERNAME_LENGTH']}~"
                                                      f"{app_config.USER_SETTINGS['MAX_USERNAME_LENGTH']}位")])
    password = StringField('password',
                           [validators.InputRequired('未填写密码'),
                            validators.Length(min=app_config.USER_SETTINGS['MIN_PWD_LENGTH'],
                                              max=app_config.USER_SETTINGS['MAX_PWD_LENGTH'],
                                              message=f"密码长度需为{app_config.USER_SETTINGS['MIN_PWD_LENGTH']}~"
                                                      f"{app_config.USER_SETTINGS['MAX_PWD_LENGTH']}位")])
    confirm_password = StringField('confirm_password',
                                   [validators.InputRequired('未填写确认密码'),
                                    validators.EqualTo('password', message='两次输入的密码不一致')])
    email = StringField('email', [validators.InputRequired(message='未填写邮箱地址'),
                                  validators.email(message='邮箱地址无效')])
    accept_agreement = BooleanField('accept_agreement')

    @staticmethod
    def validate_accept_agreement(form, field):
        if not field.data:
            raise ValidationError(message='未勾选接受用户协议')


class LoginForm(Form):
    id = StringField('id')
    username = StringField('username',
                           [validators.InputRequired('未填写用户名')])
    password = StringField('password',
                           [validators.InputRequired('未填写密码')])


class TagTemplateForm(Form):
    id = StringField('id')
    name = StringField('name',
                                    [validators.input_required('未填写标签名'),
                                     validators.Length(min=app_config.TAG_SETTINGS['MIN_TAG_NAME_LENGTH'],
                                                       max=app_config.TAG_SETTINGS['MAX_TAG_NAME_LENGTH'],
                                                       message=f"用户名长度需为{app_config.TAG_SETTINGS['MIN_TAG_NAME_LENGTH']}~"
                                                               f"{app_config.TAG_SETTINGS['MAX_TAG_NAME_LENGTH']}位")])
    field_type = StringField('field_type',
                                 [validators.input_required('未选择标签类型'),
                                  validators.any_of(app_config.TAG_SETTINGS['ALLOWED_TAG_TYPES'], '不允许的标签类型')])
    tag_group_assignment = StringField('tag_group_assignment')
    default_value = StringField('default_value')
    required = BooleanField('required')
    preview = BooleanField('preview')
    color = StringField('color')


class ReportGroupForm(Form):
    id = StringField('id')
    name = StringField('name',
                       [validators.input_required('未填写报告组名'),
                        validators.Length(min=app_config.REPORT_GROUP_SETTINGS['MIN_GROUP_NAME_LENGTH'],
                                          max=app_config.REPORT_GROUP_SETTINGS['MAX_GROUP_NAME_LENGTH'],
                                          message=f"报告组名长度需为{app_config.REPORT_GROUP_SETTINGS['MIN_GROUP_NAME_LENGTH']}~"
                                                  f"{app_config.REPORT_GROUP_SETTINGS['MAX_GROUP_NAME_LENGTH']}位")])
    open_join = BooleanField('open_join')
    color = StringField('color')
    parent_node = StringField('parent_node')


class GroupRoleForm(Form):
    id = StringField('id')
    role_abbr = StringField('role_abbr',
                            [validators.input_required('未填写角色缩写'),
                             validators.length(min=app_config.REPORT_GROUP_SETTINGS['MIN_ROLE_ABBR_LENGTH'],
                                               max=app_config.REPORT_GROUP_SETTINGS['MAX_ROLE_ABBR_LENGTH'],
                                               message=f"角色缩写长度需为{app_config.REPORT_GROUP_SETTINGS['MIN_ROLE_ABBR_LENGTH']}~"
                                                       f"{app_config.REPORT_GROUP_SETTINGS['MAX_ROLE_ABBR_LENGTH']}位")])
    role_name = StringField('role_name',
                            [validators.input_required('未填写角色名'),
                             validators.Length(min=app_config.REPORT_GROUP_SETTINGS['MIN_ROLE_NAME_LENGTH'],
                                               max=app_config.REPORT_GROUP_SETTINGS['MAX_ROLE_NAME_LENGTH'],
                                               message=f"角色名长度需为{app_config.REPORT_GROUP_SETTINGS['MIN_ROLE_NAME_LENGTH']}~"
                                                       f"{app_config.REPORT_GROUP_SETTINGS['MAX_ROLE_NAME_LENGTH']}位")])
    role_description = StringField('role_description',
                                   [validators.length(max=app_config.REPORT_GROUP_SETTINGS['MAX_DESC_LENGTH'],
                                                      message=f"描述不能多于{app_config.REPORT_GROUP_SETTINGS['MAX_DESC_LENGTH']}个字")
                                    ])
    role_color = StringField('role_color')


class TagTemplateGroupForm(Form):
    id = StringField('id')
    name = StringField('name', [validators.input_required('未填写标签组名'),
                                validators.Length(min=app_config.TAG_GROUP_SETTINGS['MIN_TAG_GROUP_NAME_LENGTH'],
                                                  max=app_config.TAG_GROUP_SETTINGS['MAX_TAG_GROUP_NAME_LENGTH'],
                                                  message=f"标签组长度需为{app_config.TAG_GROUP_SETTINGS['MIN_TAG_GROUP_NAME_LENGTH']}~"
                                                          f"{app_config.TAG_GROUP_SETTINGS['MAX_TAG_GROUP_NAME_LENGTH']}位")])
    color = StringField()
    parent_group = StringField()


class TodoItemForm(Form):
    id = StringField('id', [validators.Optional, wtforms_validators.check_mongo_oid])
    title = StringField('title', [validators.input_required('未填写待办文本'),
                        validators.Length(min=app_config.TODO_ITEM['MIN_TODO_ITEM_TITLE_LENGTH'],
                                          max=app_config.TODO_ITEM['MAX_TODO_ITEM_TITLE_LENGTH'],
                                          message=f"标签组长度需为{app_config.TODO_ITEM['MIN_TODO_ITEM_TITLE_LENGTH']}~"
                                                  f"{app_config.TODO_ITEM['MAX_TODO_ITEM_TITLE_LENGTH']}位")])
    report_group = StringField('report_group', [validators.input_required('未填写待办文本'),
                                                wtforms_validators.check_mongo_oid])