from flask import Blueprint, request, jsonify, make_response
# from flask_graphql import GraphQLView
# from flask_cors import cross_origin, CORS
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, jwt_refresh_token_required
from google.oauth2 import id_token
from google.auth.transport import requests

api = Blueprint('api', __name__)

GOOGLE_OAUTH2_CLIENT_ID = '612719863118-7j2h2p13ggleivj2a3sgbp6jrsnfchmi.apps.googleusercontent.com'

@api.route('/auth', methods = ['POST', 'OPTIONS'])
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
        
        email = id_info['email']
        name = id_info['name']
        student_id = email.split("@")[0].upper()
        
        access_token = create_access_token(email)
        # refresh_token = create_refresh_token(token)
        
        return jsonify({ 'access_token': access_token, 'student_id': student_id, 'email': email, 'name': name }), 200
    except ValueError:
        # Invalid token
        raise ValueError('Invalid token')

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
