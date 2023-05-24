from sqlite3 import IntegrityError

from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from database import RecordModel, db, UserModel, CategoryModel
from schemas import RecordSchema

blp = Blueprint("record", __name__, description="Operations on record")


@blp.route('/record')
class RecordList(MethodView):
    @jwt_required()
    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, record_data):
        if UserModel.query.filter_by(
                id=record_data.get("user_id")).first() is not None and CategoryModel.query.filter_by(
                id=record_data.get("category_id")).first() is not None:
            if record_data.get("currency_type") is not None:
                record = RecordModel(**record_data)
            else:
                currency_type = UserModel.query.filter_by(id=record_data.get("user_id")).with_entities(
                    UserModel.currency_type)
                record = RecordModel(**record_data, currency_type=currency_type)
            try:
                db.session.add(record)
                db.session.commit()
            except IntegrityError:
                abort(404, message="Record already exists")
            return record


@blp.route("/record/<string:uid>")
class Record(MethodView):
    @jwt_required()
    @blp.response(200, RecordSchema(many=True))
    def get(self, uid: str):
        record = RecordModel.query.filter_by(user_id=uid).all()
        return record

    @jwt_required()
    @blp.response(200, RecordSchema)
    def delete(self, uid: str):
        record = RecordModel.query.get_or_404(uid)
        db.session.delete(record)
        db.session.commit()
        return record


@blp.route('/record/<string:uid>/<string:cid>')
class Record(MethodView):
    @jwt_required()
    @blp.response(200, RecordSchema(many=True))
    def get(self, uid: str, cid: str):
        record = RecordModel.query.filter_by(user_id=uid, category_id=cid).all()
        return record
