# import json

# db = []
# obj1 = '{"name": "nawed", "dept": "mech", "roll": 21}'
# obj2 = '{"name": "jawed", "dept": "civil", "roll": 2}'
# obj3 = '{"name": "nawed", "dept": "mech", "roll": 14}'
# obj4 = '{"name": "jawed", "dept": "civil", "roll": 36}'

# db.append(obj1)
# db.append(obj2)
# db.append(obj3)
# db.append(obj4)
# # print(db)
# for ind, x in enumerate(db):
#     if x["roll"] == 21:
#         db.pop(ind)
# dict_object = {}
# for ind, i in enumerate(db):
#     if i["roll"] == 14:
#         dict_object = i
#         break
# y= json.load(dict_object)



# # print(dict_object)


from swagger_server.models.meal import Meal  # noqa: E501
from swagger_server import util

meal_obj = Meal()
print(meal_obj)