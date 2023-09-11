# SIMPLE REST API

## Stage Two Task
A REST API with Basic CRUD Operation
CREATE: Adding a new person.  =>/api
READ: Fetching details of a person.  => /api/user_id
UPDATE: Modifying details of an existing person => /api/user_id
DELETE: Removing a person => /api/user_id
## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation and Setup Instructions](#installation-and-setup-instructions)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [UML Diagram](#UML-Diagram)

## Prerequisites
python 3.11.5 should be installed on your machine


### Installation and Setup Instructions

1. Clone this repository:

   ```shell
   git clone https://github.com/Freeman-kuch/HNG-10
   ```

2. Navigate to the folder `cd HNG-10` in terminal or command line
   cd HNG-10

3. create a virtual environment:

    ```shell
    virtualenv venv --python=python3.11.5
    ```

4. Activate your virtual environment:

    ```shell
        <name_of_virtual_environment>\scripts\activate.bat
    ```

5. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

6. Run the Flask app:
    ```shell
    flask run
    ```

7. Open Postman, navigate to http://localhost:5000/, then you can test all endpoints with different methods like GET , POST

### usage
CREATE: Adding a new person.  (http://localhost:5000/api)
   #### METHOD: POST-> http://localhost:5000/api
    ```BODY: {
            "name": "test",
            "user_id" : 1
            "track": "backend",
            "slack_username": "test",
            "email": "test"
                }
        ```
    ###  RESPONSE:  {"message": "new user successfully created"}

READ: Fetching details of a person. (http://localhost:5000/api/<user_id>)
### Method GET: http://localhost:5000/api/<1>
### Response :    
```{"user_data":{    
            "name": "test",
            "user_id" : 1
            "track": "backend",
            "slack_username": "test",
            "email": "test"
                }
        }
```
UPDATE: Updating an existing person  (http://localhost:5000/api/<user_id>)
    ### method PATCH : http://localhost:5000/api/1
        ```BODY: {
            "name": "test",
            "user_id" : 1
            "track": "backend",
            "slack_username": "test",
            "email": "test"
                }
        ```
    Response : {"message": "user successfully Updated"}

DELETE: Deleting an existing person   (http://localhost:5000/api/<user_id>)
    ### Method DELETE: http://localhost:5000/api/<1>
        Response : {"message": "user successfully deleted"}

### Folder structure
```
HNG-10/
│
├── resource/
│   ├── __init.py__
│   ├── ennpoint.py
├── common/
│   ├── __init__.py
│   └── model.py
├── test/
│   ├── __init__.py
│   └── test_app.py
├── db.py
├── app.py
├── __init__.py
├── Procfile
├── runtime.txt
├── requirements.txt
├── wsgi.py
└── README.md
```

### UML Diagram
```
--------------------------------------
|               User                |
--------------------------------------
| - user_id: int                   |
| - name: str                      |
| - track: str                     |
| - slack_username: str            |
| - email: str                     |
--------------------------------------
| + find_user_by_id(user_id: int)  |
| + add_user(user_data: User)      |
| + update_user()                  |
| + delete_user(user_data: User)   |
--------------------------------------
```
