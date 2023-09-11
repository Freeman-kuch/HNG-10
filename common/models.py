from db import db

class User(db.Model):
    """
    Represents a model for a user in a database.

    Attributes:
        user_id (int): The primary key of the user table.
        name (str): The name of the user.
        track (str): The track of the user.
        slack_username (str): The Slack username of the user.
        email (str): The email address of the user.
    """

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    track = db.Column(db.String(30), nullable=False)
    slack_username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    @classmethod
    def find_user_by_id(cls, user_id: int) -> 'User':
        """
        Finds a user by their ID and returns the user object.

        Args:
            user_id (int): The ID of the user to find.

        Returns:
            User: The user object.

        Raises:
            NotFound: If no user with the given ID is found.
        """
        return cls.query.get_or_404(user_id)

    @classmethod
    def find_user_by_name(cls, name: str) -> 'User':
        """
        Finds a user by their name and returns the user object.

        Args:
            name (str): The name of the user to find.

        Returns:
            User: The user object.

        Raises:
            NotFound: If no user with the given name is found.
        """
        return cls.query.get_or_404(name)

    @classmethod
    def add_user(cls, user_data: 'User') -> None:
        """
        Adds a new user to the database.

        Args:
            user_data (User): The user object to add.
        """
        db.session.add(user_data)
        db.session.commit()

    def update_user(self) -> None:
        """
        Commits any changes made to the user object in the database.
        """
        db.session.commit()

    @classmethod
    def delete_user(cls, user_data: 'User') -> None:
        """
        Deletes a user from the database.

        Args:
            user_data (User): The user object to delete.
        """
        db.session.delete(user_data)
        db.session.commit()

