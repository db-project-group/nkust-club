import os
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from view.api import api
from db.manage import db_data
from db.model import *


def create_app(dist_path="dist"):
    app = Flask(__name__,
                static_folder=os.path.join(dist_path, "static"),
                template_folder=dist_path)
    
    app.config.from_object(Config)
    
    # Frontend route
    @app.route('/')
    def index():
        return render_template("index.html")

    # Blueprint
    app.register_blueprint(api, url_prefix='/api/v1')
    app.register_blueprint(db_data)

    return app


app = create_app("./dist")
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

if __name__ == "__main__":
    app.run()
