from flask import Flask
from flask_restful import Api

from db import db
from config import Config
from resources.user_resources import UserList, User

app = Flask(__name__)
api = Api(app)
config = Config()


@app.before_first_request
def setup_db():
    uri = f"postgresql://{config.db_user}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_name}"
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    db.init_app(app)
    db.create_all()


api.add_resource(UserList, "/users")
api.add_resource(User, "/users/<int:id>")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=config.db_port)
