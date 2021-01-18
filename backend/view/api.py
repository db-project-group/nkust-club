from flask import Blueprint, request, jsonify, make_response
# from flask_graphql import GraphQLView
# from flask_cors import cross_origin, CORS
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, jwt_refresh_token_required
from google.oauth2 import id_token
from google.auth.transport import requests
from controller.club import ClubController

api = Blueprint('api', __name__)

GOOGLE_OAUTH2_CLIENT_ID = '612719863118-7j2h2p13ggleivj2a3sgbp6jrsnfchmi.apps.googleusercontent.com'

@api.route('/auth', methods = ['POST'])
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
        
        access_token = create_access_token(student_id)
        # refresh_token = create_refresh_token(token)
        
        return jsonify({'access_token': access_token, 'student_id': student_id, 'email': email, 'name': name}), 200
    except ValueError:
        # Invalid token
        raise ValueError('Invalid token')


@api.route('/auth/refresh', methods=['POST'])
@jwt_refresh_token_required
def auth_refresh():
    student_id = get_jwt_identity()
    return jsonify({'access_token': create_access_token(student_id)}), 200


@api.route('/club', methods=['GET'])
@jwt_required
def get_clubs():
    student_id = get_jwt_identity()
    rs = ClubController.get_clubs(student_id)
    return jsonify(clubs=rs), 200


@api.route('/club/<int:club_id>', methods=['GET'])
@jwt_required
def get_club(club_id):
    student_id = get_jwt_identity()
    
    rs = ClubController.get_club(student_id, club_id)
    if rs == -1:
        return jsonify(), 403
    return jsonify(club=rs), 200


# api.add_url_rule('/graphql', view_func=GraphQLView.as_view(
#     'graphql',
#     schema=schema,
#     graphiql=True,
# ))
