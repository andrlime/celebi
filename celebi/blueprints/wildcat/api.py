"""
API routes for parser blueprint
"""

import requests

from http import HTTPStatus
from flask import Blueprint, request, Response
from flask_cors import cross_origin

from celebi.core.config import AppConfig
from celebi.core.util import make_json_response
from celebi.core.util import get_body_field
from celebi.core.exceptions import RequestValueError


bp = Blueprint("wildcat", __name__)


@bp.route("/subscribe", methods=["POST", "OPTIONS"])
@cross_origin(origins="https://wildhacks.net")
def subscribe_new_email() -> Response:
    """
    Subscribes a new user to the Wildhacks email list

    Deprecated! A new route is needed for WildHacks 2026. The code for the existing route
    can be found in the commit history of this repository.
    """

    return make_json_response("WildHacks 2025 is over. Please subscribe to the mailing list for WildHacks 2026.", HTTPStatus.BAD_REQUEST)
