# SIMPLE REST API

## Stage Two Task
A REST API with Basic CRUD Operations
- **CREATE:** Adding a new person => `/api`
- **READ:** Fetching details of a person => `/api/name`
- **UPDATE:** Modifying details of an existing person => `/api/name`
- **DELETE:** Removing a person => `/api/name`

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation and Setup Instructions](#installation-and-setup-instructions)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [UML Diagram](#uml-diagram)

## Prerequisites
- Python 3.11.5 should be installed on your machine.

### Installation and Setup Instructions

1. Clone this repository:

   ```shell
   git clone https://github.com/Freeman-kuch/HNG-10
   ```

2. Navigate to the folder `cd HNG-10` in the terminal or command line:
   ```shell
   cd HNG-10
   ```

3. Create a virtual environment:

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

7. Open Postman, navigate to `http://localhost:5000/`, then you can test all endpoints with different methods like GET, POST.

### Usage

**CREATE:** Adding a new person. (http://localhost:5000/api)
- **METHOD:** POST -> http://localhost:5000/api

   **BODY:**
   ```json
   {
       "name": "test",
       // the following fields are optional
      // "user_id": 1,
      // "track": "backend",
       //"slack_username": "test",
      // "email": "test"
   }
  ```
   **RESPONSE:**  
   ```json
    "new_user": {
        {
         "name": "test",
         "user_id": 1,
         "track": "null",
         "slack_username": "null",
         "email": "null"
      }
    }
  ```


**READ:** Fetching details of a person. (http://localhost:5000/api/<string :name>)
- **Method GET:** http://localhost:5000/api/test

   **RESPONSE:**
   ```json
   {"user_data": {
       "name": "test",
       "user_id": 1,
       "track": "null",
       "slack_username": "null",
       "email": "null"
       }
   }
   ```

**UPDATE:** Updating an existing person (http://localhost:5000/api/<string: name>)
- **Method PATCH:** http://localhost:5000/api/test

   **BODY:**
   ```json
   {
       "name": "another test",
       "user_id": 1,
       "track": "backend",
       "slack_username": "test",
       "email": "test"
   }
   ```

   **RESPONSE:**  
   ```json
    "user_updated": {
        {
         "name": "another test",
         "user_id": 1,
         "track": "backend",
         "slack_username": "test",
         "email": "test"
      }
    }
  ```

**DELETE:** Deleting an existing person (http://localhost:5000/api/<string: name>)
- **Method DELETE:** http://localhost:5000/api/another test

   **RESPONSE:**  
   ```json
    "user_deleted": {
        {
         "name": "another test",
         "user_id": 1,
         "track": "backend",
         "slack_username": "test",
         "email": "test"
      }
    }
  ```

### Folder Structure

```plaintext
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

```plaintext
--------------------------------------
|               User                |
--------------------------------------
| - user_id: int                   |
| - name: str                      |
| - track: str                     |
| - slack_username: str            |
| - email: str                     |
--------------------------------------
| + find_user_by_name(name: str)  |
| + add_user(user_data: User)      |
| + update_user()                  |
| + delete_user(user_data: User)   |
--------------------------------------
```

