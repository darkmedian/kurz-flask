import hashlib
from flask import Blueprint, jsonify, request
from app.api.models import Shortner
from app import db
from sqlalchemy import exc

shortner_blueprint = Blueprint('shortner', __name__)


@shortner_blueprint.route('/shortner/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@shortner_blueprint.route('/shortner', methods=['GET'])
def get_all_shortner():
    """Get all shortner"""
    response_object = {
        'status': 'success',
        'data': {
            'shortner': [url_shortner.to_json() for url_shortner in Shortner.query.all()]
        }
    }
    return jsonify(response_object), 200


@shortner_blueprint.route('/shortner', methods=['POST'])
def add_user():
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }
    if not post_data:
        return jsonify(response_object), 400
    url = post_data.get('url')
    digest = hashlib.md5(url.encode('utf-8')).hexdigest()[:6]
    try:
        url_shortner = Shortner.query.filter_by(digest=digest).first()
        if not url_shortner:
            db.session.add(Shortner(url=url, digest=digest))
            db.session.commit()
            response_object['status'] = 'success'
            response_object['message'] = digest
            return jsonify(response_object), 201
        else:
            response_object['message'] = 'Sorry. That url already exists.'
            return jsonify(response_object), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(response_object), 400


@shortner_blueprint.route('/shortner/<digest>', methods=['GET'])
def get_single_user(digest):
    """Get single URL details"""
    response_object = {
        'status': 'fail',
        'message': 'URL does not exist'
    }
    try:
        url_shortner = Shortner.query.filter_by(digest=str(digest)).first()
        if not url_shortner:
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                    'url': url_shortner.url,
                    'digest': url_shortner.digest,
                }
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
