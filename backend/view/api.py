from flask import Blueprint
# from flask_graphql import GraphQLView


api = Blueprint('api', __name__)

@api.route('/auth')
def auth():
    return 'aaa'

# api.add_url_rule('/graphql', view_func=GraphQLView.as_view(
#     'graphql',
#     schema=schema,
#     graphiql=True,
# ))
