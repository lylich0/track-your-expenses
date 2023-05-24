from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    currency_type = fields.Str(required=False)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    date = fields.Str(dump_only=True)
    amount = fields.Str(required=True)
    currency_type = fields.Str(required=False)


class CurrencySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)