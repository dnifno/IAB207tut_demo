from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import datetime

# need to register each blueprint here

db = SQLAlchemy()
app = Flask(__name__)


def create_app():
    Bcrypt(app)

    bootstrap = Bootstrap5(app)  # utility module used to display forms quickly
    app.secret_key = "secretKey123!"  # session object secret key

    # configue and initialise DB
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///traveldb.sqlite"
    db.init_app(app)

    # add Blueprints
    from . import views

    app.register_blueprint(views.mainbp)

    from . import destinations

    app.register_blueprint(destinations.destbp)

    from . import auth

    app.register_blueprint(auth.authbp)

    # initialise login authentication
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    # create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # config upload folder
    UPLOAD_FOLDER = "/static/image"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    @app.errorhandler(404)
    # inbuilt function which takes error as parameter
    def not_found(e):
        return render_template("404.html", error=e)

    # @app.errorhandler(500) ALSO IMPLEMENT ERROR CODE 500
    @app.errorhandler(500)
    def internal_server_error(e):
        # note that we set the 500 status explicitly
        return render_template("500.html", error=e)

    # this creates a dictionary of variables that are available
    # to all html templates
    @app.context_processor
    def get_context():
        year = datetime.datetime.today().year
        return dict(year=year)

    return app
