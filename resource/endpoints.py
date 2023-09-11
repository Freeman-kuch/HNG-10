from typing import Dict, Any
from flask_restful import Resource, fields, marshal_with, reqparse
from common.model import user
import datetime
import json


hng_10 = reqparse.RequestParser()
hng_10.add_argument("name", type=str, required=True, help="This field can't be left Blank",)
hng_10.add_argument("user_id", type=int, required=True, help="This field can't be left Blank")
hng_10.add_argument("track", type=str, required=True, help="This field can't be left Blank")
hng_10.add_argument("slack_username", type=str, required=True, help="This field can't be left Blank")
hng_10.add_argument("email", type=str, required=False,)

Users_fields = {
    "user_id": fields.Integer,
    "slack_username": fields.String,
    "track": fields.String,
    "name": fields.String,
    "email": fields.String,
}



# ================MODIFY========================
class bio(Resource):
    """
    A Flask-Restful resource that handles HTTP POST requests.
    
    Parses the request arguments using the `hng_10` request parser and extracts the required data.
    Creates a new instance of the `items` class with the extracted data and adds it to the database.
    Returns a success message if the new user is added successfully.
    """
    
    def post(self):
        # ======CREATE==============
        """
        Handles the HTTP POST request.
        
        Parses the request arguments, extracts the required data, creates a new instance of the `items` class,
        adds it to the database, and returns a success message.
        
        Returns:
            dict: A dictionary containing a success message if the new user is added successfully.
        
        Raises:
            ValueError: If an error occurs during the process.
        """
        
        req_data = hng_10.parse_args()
        user_data = {"name": req_data.get("name"),
                     "track": req_data.get("track"),
                     "slack_username": req_data.get("slack_username"),
                     "email": req_data.get("email"),
                     }
        
        new_user = user(**user_data)
        try:
            #  =======DATABASE==========
            user.add_user(new_user)
        except ValueError as exc:
            return {"error": "Failed"}, 400
        return {"message": "new user successfully created"}, 201    




class stage_2(Resource):
        # ======   READ ==========
    @marshal_with(Users_fields, envelope="user_data")
    def get(self, name: str) -> Dict[str, Any]:
        """
        Retrieves a user's information based on their name.

        Args:
            name: The name of the user to retrieve information for.

        Returns:
            A dictionary containing the user's information, wrapped in the 'user_data' key.
        """
        user_data = user.find_user_by_name(name)
        return {"user_data": user_data}, 202


    def patch(self, name: str) -> dict:
        """
        Update the information of a user based on their name.

        Args:
            name (str): The ID of the user to be updated.

        Returns:
            dict: A dictionary with the message "item successfully Updated" and the status code 201.
        """
        update_data = user.find_user_by_name(name)
        req_data = hng_10.parse_args()

        for key, value in req_data.items():
            setattr(update_data, key, value)

        user.updating_user()

        return {"message": "item successfully Updated"}, 202


    def delete(self, name: int) -> dict:
        """
        Deletes a user's information based on their name.

        Args:
            name (str): The ID of the user to be deleted.

        Returns:
            dict: A dictionary with the message "item successfully deleted" and the status code 204.
        """
        delete_data = user.find_user_by_name(name)
        user.delete_user(delete_data)
        return {"message": "item successfully deleted"}, 204


