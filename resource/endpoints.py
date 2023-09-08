from flask_restful import Resource, fields, marshal_with, reqparse
import datetime
import json

parser = reqparse.RequestParser()
parser.add_argument('slack_name', type=str, help='slack_name', location="args")
parser.add_argument('track', type=str, help='track', location="args")



bio_fields = {
            "slack_name": fields.String,
            "current_day":  fields.String,
            "utc_time": fields.String,
            "track": fields.String,
            "github_file_url": fields.String,
            "github_repo_url": fields.String,
            "status_code": fields.Integer,
}


class bio(Resource):
    @marshal_with(bio_fields)
    def get(self):

        args = parser.parse_args()


        time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        day = time.strftime('%A')



        data = {
            "slack_name": args.get("slack_name"),
            "current_day":  str(day),
            "utc_time": str(time),
            "track": args.get("track"),
            "github_file_url": "https://github.com/Freeman-kuch/HNG-10/blob/main/app.py",
            "github_repo_url": "https://github.com/Freeman-kuch/HNG-10",
            "status_code": 200,
        }
        return data, 200