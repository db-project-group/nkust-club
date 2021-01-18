from flask import Blueprint
from flask_graphql import GraphQLView
from flask import jsonify
from flask import request
from google.oauth2 import id_token
from google.auth.transport import requests
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, jwt_refresh_token_required

GOOGLE_OAUTH2_CLIENT_ID = '687495968491-6k4toog7o8ajqvie4mj28pjnbkgnishm.apps.googleusercontent.com'
api = Blueprint('api', __name__)

@api.route('/auth', methods = ['post'])
def auth():
    token = request.json['id_token']
    try:
        id_info = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            GOOGLE_OAUTH2_CLIENT_ID
        )
        if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
    except ValueError:
        # Invalid token
        raise ValueError('Invalid token')
 
    access_token = create_access_token(token)
    refresh_token = create_refresh_token(token)
    return jsonify({'access_token': access_token}), 200

@api.route('/JWT_access_token', methods = ['post'])
@jwt_required
def JWT_access():
    username = get_jwt_identity()
    return jsonify(loggin_in_as = username), 200

@api.route('/JWT_refresh_token', methods = ['post'])
@jwt_refresh_token_required
def JWT_refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200



# api.add_url_rule('/graphql', view_func=GraphQLView.as_view(
#     'graphql',
#     schema=schema,
#     graphiql=True,
# ))
