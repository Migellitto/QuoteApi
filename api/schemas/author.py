from api import ma
from api.models.author import AuthorModel
from api.models.quote import QuoteModel


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AuthorModel


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
