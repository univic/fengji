# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-01-31

from wtforms import Form, BooleanField, StringField, validators, ValidationError
from app.config import app_config


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
    username = StringField('username',
                           [validators.InputRequired('未填写用户名')])
    password = StringField('password',
                           [validators.InputRequired('未填写密码')])


class NewTagForm(Form):
    tagName = StringField('tagName',
                           [validators.input_required('未填写标签名'),
                            validators.Length(min=app_config.TAG_SETTINGS['MIN_TAG_NAME_LENGTH'],
                                              max=app_config.TAG_SETTINGS['MAX_TAG_NAME_LENGTH'],
                                              message=f"用户名长度需为{app_config.TAG_SETTINGS['MIN_TAG_NAME_LENGTH']}~"
                                                      f"{app_config.TAG_SETTINGS['MAX_TAG_NAME_LENGTH']}位")])
    tagFieldType = StringField('tagFieldType',
                           [validators.input_required('未选择标签类型'),
                            validators.any_of(app_config.TAG_SETTINGS['ALLOWED_TAG_TYPES'], '不允许的标签类型')])
    tagDefaultValue = StringField('tagDefaultValue')
    tagPreview = BooleanField('tagPreview')
    tagColor = StringField('tagColor')
