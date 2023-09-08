from flask_restful import Resource, fields, marshal_with, reqparse
import datetime
import json

parser = reqparse.RequestParser()
parser.add_argument('slack_name', type=str, help='slack_name', location="args")
parser.add_argument('track', type=str, help='track', location="args")



bio_fields = {
            "Slack Name": fields.String,
            "Current Day of the Week":  fields.String,
            "Current UTC Time": fields.String,
            "Track": fields.String,
            "GitHub File URL": fields.String,
            "GitHub Repo URL": fields.String,
            "Status Code": fields.Integer,
}


class bio(Resource):
    @marshal_with(bio_fields)
    def get(self):

        args = parser.parse_args()


        time = datetime.datetime.utcnow()
        day = time.strftime('%A')



        data = {
            "Slack Name": args.get("slack_name"),
            "Current Day of the Week":  str(day),
            "Current UTC Time": str(time),
            "Track": args.get("track"),
            "GitHub File URL": "https://github.com/Freeman-kuch/HNG-10/blob/main/app.py",
            "GitHub Repo URL": "https://github.com/Freeman-kuch/HNG-10",
            "Status Code": 200,
        }
        return data, 200