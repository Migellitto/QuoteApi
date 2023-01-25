from api import app, db, request
from api.models.author import AuthorModel
from api.schemas.author import author_schema, authors_schema
from api.schemas.quote import quote_schema, quotes_schema
from api.models.quote import QuoteModel


@app.route('/authors', methods=["GET"])
def get_authors():
    authors = AuthorModel.query.all()
    # authors_dict = [author.to_dict() for author in authors]
    # return authors_dict, 200
    return authors_schema.dump(authors), 200


@app.route('/authors/<int:author_id>', methods=["GET"])
def get_author_by_id(author_id):
    author = AuthorModel.query.get(author_id)
    # if not author:
    #     return f"Author id={author_id} not found", 404

    # return author.to_dict(), 200
    return author_schema.dump(author)


@app.route('/authors', methods=["POST"])
def create_author():
    author_data = request.json
    author = AuthorModel(author_data["name"])
    db.session.add(author)
    db.session.commit()
    # return author.to_dict(), 201
    return author_schema.dump(author)


@app.route('/authors/<int:author_id>', methods=["PUT"])
def edit_author(author_id):
    author_data = request.json
    author = AuthorModel.query.get(author_id)
    if author is None:
        return {"Error": f"Author id={author_id} not found"}, 404
    author.name = author_data["name"]
    db.session.commit()
    # return author.to_dict(), 200
    return author_schema.dump(author)


@app.route('/authors/<int:author_id>', methods=["DELETE"])
def delete_author(author_id):
    author = AuthorModel.query.get(author_id)
    if author is None:
        return f"Author with id={author_id} not found", 404
    # Удаляем автора у которого нет цитат.
    # Если есть цитаты у автора, то автор будет удален, а цитаты нет.
    # Вместо id автора появится значение NULL в колонке автора.
    db.session.delete(author)
    db.session.commit()
    return {"message": f"Author with id={author_id} has deleted"}, 200
