from flask import jsonify
from flask_restful import reqparse, Resource
from mongoengine import NotUniqueError
from validate_docbr import CPF
from .model import UserModel


_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('last_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('cpf',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('birth_date',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )


cpf = CPF()


class Users(Resource):
    def get(self):
        return jsonify(UserModel.objects())


class User(Resource):
    def post(self):
        data = _user_parser.parse_args()

        if not cpf.validate(data["cpf"]):
            return {"message": "CPF is invalid!"}, 400

        try:
            response = UserModel(**data).save()
            return {"message": "User %s successfully created!" % response.id}
        except NotUniqueError:
            return {"message": "CPF already exists in database!"}

    def get(self, cpf):
        response = UserModel.objects(cpf=cpf)

        if response:
            return jsonify(response)
        else:
            return {"message": "User does not exist in database!"}, 400

    def patch(self):
        data = _user_parser.parse_args()

        if not cpf.validate(data["cpf"]):
            return {"message": "CPF is invalid!"}, 400

        response = UserModel.objects(cpf=data["cpf"])
        if response:
            response.update(**data)
            return {"message": "User updated!"}, 200
        else:
            return {"message": "User does not exist in database!"}, 400
