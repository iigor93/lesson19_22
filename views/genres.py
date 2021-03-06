""" views для модели Genres. GET, PUT, POST, DELETE"""


from flask_restx import Resource, Namespace
from flask import request
from dao.model.genre import GenreSchema
from implemented import genre_service
from service.decorators import admin_required, auth_required


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        data = request.json
        genre_service.create(data)
        return "", 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, rid):
        data = request.json
        genre_service.update(data)
        return "", 201

    @admin_required
    def delete(self, rid):
        genre_service.delete(rid)
        return "", 204
