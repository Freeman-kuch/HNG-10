from typing import Dict, Any
from flask_restful import Resource, fields, marshal_with, reqparse
from common.models import user

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="This field can't be left blank")
parser.add_argument("user_id", type=int, required=False, help="This field can't be left blank")
parser.add_argument("track", type=str, required=True, help="This field can't be left blank")
parser.add_argument("slack_username", type=str, required=True, help="This field can't be left blank")
parser.add_argument("email", type=str)

users_fields = {
    "user_id": fields.Integer,
    "slack_username": fields.String,
    "track": fields.String,
    "name": fields.String,
    "email": fields.String,
}



class bio(Resource):
    """
    A Flask-Restful resource that handles HTTP POST requests.
    
    Parses the request arguments using the `parser` request parser and extracts the required data.
    Creates a new instance of the `items` class with the extracted data and adds it to the database.
    Returns a success message if the new user is added successfully.
    """
    
    def post(self) -> dict:
        """
        Handles the HTTP POST request.

        Parses the request arguments, extracts the required data, creates a new instance of the `user` class,
        adds it to the database, and returns a success message.

        Args:
            req_data (dict): A dictionary containing the request data, including the user's name, track, Slack username, and email.

        Returns:
            dict: A dictionary containing a success message if the new user is added successfully.

        Raises:
            ValueError: If an error occurs during the process.
        """
        req_data = parser.parse_args()

        user_data = {
            "name": req_data.get("name"),
            "track": req_data.get("track"),
            "slack_username": req_data.get("slack_username"),
            "email": req_data.get("email"),
        }

        new_user = user(**user_data)
        try:
            user.add_user(new_user)
        except ValueError as exc:
            return {"error": "Failed"}, 400

        return {"message": "new user successfully created"}, 201



class stage_2(Resource):
        # ======   READ ==========
    @marshal_with(users_fields, envelope="user_data")
    def get(self, user_id: int) -> Dict[str, Any]:
        """
        Retrieves a user's information based on their user_id.

        Args:
            name: The name of the user to retrieve information for.

        Returns:
            A dictionary containing the user's information, wrapped in the 'user_data' key.
        """
        user_data = user.find_user_by_id(user_id=user_id)
        return  user_data, 200


    def patch(self, user_id: int) -> dict:
        """
        Update the information of a user based on their name.

        Args:
            user_id (int): The ID of the user to be updated.

        Returns:
            dict: A dictionary with the message "item successfully Updated" and the status code 201.
        """
        update_data = user.find_user_by_id(user_id)
        req_data = parser.parse_args()

        for key, value in req_data.items():
            setattr(update_data, key, value)

        user.update_user()

        return {"message": "user successfully Updated"}, 202


    def delete(self, user_id: int) -> dict:
        """
        Deletes a user's information based on their name.

        Args:
            name (str): The ID of the user to be deleted.

        Returns:
            dict: A dictionary with the message "item successfully deleted" and the status code 204.
        """
        delete_data = user.find_user_by_id(user_id)
        user.delete_user(delete_data)
        return {"message": "user successfully deleted"}, 200


