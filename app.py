from api import app
from api.handlers import author
from api.handlers import quote
from config import Config
from api.handlers import user
from api.handlers import token


if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)
