from distutils.command.build_scripts import first_line_re
from flask_restful import Resource, fields, marshal_with

bio_fields = {
    "SlackUsername": fields.String,
    "backend": fields.Boolean,
    "Age": fields.Integer,
    "Bio": fields.String
}


class bio(Resource):
    @marshal_with(bio_fields, envelope="My Bio")
    def get(self):
        return {
            "SlackUsername": "Freeman",
            "backend": True,
            "Age": 24,
            "Bio": "I'm  a Backend engineer from Lagos, Nigeria. I am  always willing and ready to learn and add value to the community",
        }
