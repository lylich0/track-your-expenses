import os
from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from database import db, CurrencyModel
from resources.user import blp as UserBlueprint
from resources.category import blp as CategoryBlueprint
from resources.record import blp as RecordBlueprint
from resources.currency import blp as CurrencyBlueprint


def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'system.db')
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "SSDT|REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    db.init_app(app)

    api = Api(app)
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    api.register_blueprint(UserBlueprint)
    api.register_blueprint(CategoryBlueprint)
    api.register_blueprint(RecordBlueprint)
    api.register_blueprint(CurrencyBlueprint)

    with app.app_context():
        db.drop_all()
        db.create_all()

        if len(CurrencyModel.query.all()) == 0:
            currency_1 = CurrencyModel(name="Hryvnia")
            currency_2 = CurrencyModel(name="Dollar")
            currency_3 = CurrencyModel(name="Euro")

            for currency in [currency_1, currency_2, currency_3]:
                db.session.add(currency)
            db.session.commit()

    return app


app = create_app()
