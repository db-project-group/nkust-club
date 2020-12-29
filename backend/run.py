import os
from flask import Flask, render_template
from view.api import api
from config import Config


def create_app(dist_path="dist"):
    app = Flask(__name__,
                static_folder=os.path.join(dist_path, "static"),
                template_folder=dist_path)
    
    app.config.from_object(Config)

    # Frontend route
    @app.route('/')
    def index():
        return render_template("index.html")

    # Api blueprint
    app.register_blueprint(api, url_prefix='/api/v1')
    
    return app

if __name__ == "__main__":
    app = create_app("../frontend/dist")
    app.run()
