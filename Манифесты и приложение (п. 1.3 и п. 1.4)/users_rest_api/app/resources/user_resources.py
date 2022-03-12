from flask_restful import reqparse, fields, Resource, marshal_with, abort

from db import db
from models.user_model import UserModel

parser = reqparse.RequestParser()
parser.add_argument("firstname", type=str)
parser.add_argument("lastname", type=str)
parser.add_argument("age", type=int)
RESOURCE_FIELDS = {
    "id": fields.Integer,
    "firstname": fields.String,
    "lastname": fields.String,
    "age": fields.Integer,
}


class UserList(Resource):
    """Handles .../users"""

    @marshal_with(RESOURCE_FIELDS)
    def get(self):
        """Returns list of all users"""
        data = UserModel.query.all()
        return data, 200

    @marshal_with(RESOURCE_FIELDS)
    def post(self):
        """Creates a user with given parameters"""
        args = parser.parse_args(strict=True)

        user = UserModel(
            firstname=args["firstname"],
            lastname=args["lastname"],
            age=args["age"],
        )
        db.session.add(user)
        db.session.commit()

        return user, 201


class User(Resource):
    """Handles .../users/id"""

    @marshal_with(RESOURCE_FIELDS)
    def get(self, id: int):
        """Returns a user with specified id"""

        result = UserModel.query.filter_by(id=id).first()
        if result:
            return result
        abort(404, message=f"User wth id={id} does not exist")

    @marshal_with(RESOURCE_FIELDS)
    def put(self, id: int):
        """Changes a user with specified id"""

        args = parser.parse_args()
        query = UserModel.query.filter_by(id=id)
        if not query.first():
            abort(404, message=f"User wth id={id} does not exist")

        query.update(args)
        db.session.commit()

        return query.first(), 201

    @marshal_with(RESOURCE_FIELDS)
    def delete(self, id: int):
        """Deletes a user with specified id"""

        if not UserModel.query.filter_by(id=id).first():
            abort(404, message=f"User with id={id} does not exist")

        UserModel.query.filter_by(id=id).delete()
        db.session.commit()
        return 204
