from sqlite3 import IntegrityError

from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from database import db, CurrencyModel
from schemas import CurrencySchema

blp = Blueprint("currency", __name__, description="Operations on currency")


@blp.route('/currency')
class CurrencyList(MethodView):
    @jwt_required()
    @blp.response(200, CurrencySchema(many=True))
    def get(self):
        return CurrencyModel.query.all()

    @jwt_required()
    @blp.arguments(CurrencySchema)
    @blp.response(200, CurrencySchema)
    def post(self, currency_data):
        currency = CurrencyModel(**currency_data)
        try:
            db.session.add(currency)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Currency already exists")
        return currency