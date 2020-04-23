import connexion
import six
import json

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def load_db():
    with open('swagger_server\data\data_user.json') as f:
        return json.load(f)


def load_user():
    with open('swagger_server\data\logged_users.json') as f:
        return json.load(f)


users = load_db()
logged_users = load_user()


def create_user(body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    users = load_db()
    users.append(body)
    json_object = json.dumps(users)
    with open("swagger_server\data\data_user.json", "w") as outfile:
        outfile.write(json_object)

    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'User added', 201


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """

    users = load_db()
    for ind, i in enumerate(users):
        if str(i["username"]) == username:
            users.pop(ind)
    json_object = json.dumps(users)
    with open("swagger_server\data\data_user.json", "w") as outfile:
        outfile.write(json_object)

    return 'deleted user', 202


def get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing. 
    :type username: str

    :rtype: User
    """
    dict_obj = {}
    users = load_db()
    for ind, i in enumerate(users):
        if str(i["username"]) == username:
            dict_obj = i
            break

    return dict_obj, 200


def login_user(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    logged_users = load_user()
    users = load_db()
    for ind, i in enumerate(users):
        if (str(i["username"]) == username) and (str(i["password"] == password)):
            logged_users.append({"username": username, "password": password})
            json_object = json.dumps(logged_users)
            with open("swagger_server\data\logged_users.json", "w") as outfile:
                outfile.write(json_object)
            return "Looged In", 200

    return 'Username or Password is wrong'


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    logged_users = load_user()
    if len(logged_users > 0):
        logged_users.clear()
        json_object = json.dumps(logged_users)
        with open("swagger_server\data\logged_users.json", "w") as outfile:
            outfile.write(json_object)
        return "logged out", 200

    return 'No one logged in', 200


def update_user(username, body):  # noqa: E501
    """Updated user

    This can only be done by the logged in user. # noqa: E501

    :param username: name that need to be updated
    :type username: str
    :param body: Updated user object
    :type body: dict | bytes

    :rtype: None
    """
    flag = 0
    users = load_db()
    for ind, i in enumerate(users):
        if str(i["username"]) == username:
            users[ind] = body
            json_object = json.dumps(users)
            with open("swagger_server\data\data_user.json", "w") as outfile:
                outfile.write(json_object)
            flag = 1

    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    if flag == 1:
        return 'Updated', 200
    else:
        return "Incorrect Username", 200
