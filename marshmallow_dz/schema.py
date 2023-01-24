from marshmallow import Schema, fields


class LearnerSchema(Schema):
    uid = fields.Integer()
    name = fields.Str(required=True)
    final_test = fields.Boolean(required=True)
