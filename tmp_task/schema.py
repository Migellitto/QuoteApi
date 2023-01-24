from marshmallow import Schema, fields


class AuthorSchema(Schema):
    id = fields.Integer()
    name = fields.Str(required=True)  # required - обязательное значение
    email = fields.Str(required=True, error_messages={
                       'required': 'email is required'})
