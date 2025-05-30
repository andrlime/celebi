"""
API routes for parser blueprint
"""

from http import HTTPStatus
from flask import Blueprint, Response
from flask_cors import cross_origin

from celebi.core.util import make_json_response


bp = Blueprint("root", __name__)


@bp.route("/", methods=["GET"])
@cross_origin(origins="*")
def get_root_page() -> Response:
    """
    Template route
    """

    return make_json_response("Hello world! v1.1-20252905a", HTTPStatus.OK)
