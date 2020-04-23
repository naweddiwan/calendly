import connexion
import six
from flask import Flask, jsonify
from swagger_server.models.meal import Meal  # noqa: E501
from swagger_server import util
import json


def load_db():
    with open("swagger_server\data\data.json") as f:
        return json.load(f)

def add_meal(body):  # noqa: E501
    """Add meal

    This can only be done by the logged in user. # noqa: E501

    :param body: Meal object to Add
    :type body: dict | bytes

    :rtype: None
    """
    meals = load_db()
    meals.append(body)
    json_object = json.dumps(meals)
    with open("swagger_server\data\data.json", "w") as outfile:
        outfile.write(json_object)
    if connexion.request.is_json:
        body = Meal.from_dict(connexion.request.get_json())  # noqa: E501
    for i in meals:
        print(i)
    return 'meal added', 201


def delete_meal(meal_id):  # noqa: E501
    """Delete meal entry

    This can only be done by the logged in user. # noqa: E501

    :param meal_id: The meal that needs to be deleted.
    :type meal_id: str

    :rtype: None
    """
    meals = load_db()
    for ind, i in enumerate(meals):
        if str(i["meal_id"]) == meal_id:
            meals.pop(ind)
            json_object = json.dumps(meals)
            with open("swagger_server\data\data.json", "w") as outfile:
                outfile.write(json_object)
            break
    for i in meals:
        print(i)
    return 'meal deleted', 202


def get_meal_by_meal_id(meal_id):  # noqa: E501
    """Get meal by meal id

    Get Meal by specifying the meal ID # noqa: E501

    :param meal_id: The meal that needs to be fetched.
    :type meal_id: str

    :rtype: Meal
    """
    meals = load_db()
    dict_object = {}
    for ind, i in enumerate(meals):
        if str(i["meal_id"]) == meal_id:
            dict_object = i
            break
    # json_obj = jsonify(dict_object)
    for i in meals:
        print(i)
    return dict_object, 200


def update_meal(meal_id, body):  # noqa: E501
    """Update Meal entry

    This can only be done by the logged in user. # noqa: E501

    :param meal_id: meal that needs to be updated
    :type meal_id: str
    :param body: Updated meal object
    :type body: dict | bytes

    :rtype: None
    """
    for ind, i in enumerate(meals):
        if str(i["meal_id"]) == meal_id:
            meals[ind] = body
            json_object = json.dumps(meals)
            with open("swagger_server\data\data.json", "w") as outfile:
                outfile.write(json_object)
            break
    for i in meals:
        print(i)
    if connexion.request.is_json:
        body = Meal.from_dict(connexion.request.get_json())  # noqa: E501
    return "updated", 200
