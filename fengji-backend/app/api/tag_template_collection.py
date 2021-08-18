from mongoengine.errors import NotUniqueError, ValidationError
from flask import Blueprint, request, jsonify
from app.model.tag_template import TagTemplate
from app.model.tag_template_group import TagTemplateGroup
from flask_jwt_extended import get_jwt_identity, jwt_required, current_user, get_current_user
from app.model.post_forms import TagTemplateForm

bp = Blueprint('tag_template_collection', __name__, url_prefix='/api/tag_template_collection')


@bp.route('/', methods={'GET'})
@jwt_required()
def get_tag_template_collection():
    pass


@bp.route('/', methods={'POST'})
@jwt_required()
def add_tag_template_collection():
    pass


@bp.route('/', methods={'PUT'})
@jwt_required()
def modify_tag_template_collection():
    pass


@bp.route('/', methods={'DELETE'})
@jwt_required()
def delete_tag_template_collection():
    pass