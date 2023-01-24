from author import Author
from schema import AuthorSchema

# author = Author(1, "Alex", "alex5@mail.ru")
authors = [
    Author(1, "Alex", "alex1@mail.ru"),
    Author(1, "Xela", "alex2@mail.ru"),
    Author(1, "Xlea", "alex3@mail.ru")
]
author_schema = AuthorSchema(many=True)
result = author_schema.dump(authors)
print(result, type(result))
