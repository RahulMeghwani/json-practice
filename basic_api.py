from flask import Flask, request, jsonify

app = Flask(__name__)

import json
with open("json-files/data.json", "r") as f:
    data = json.load(f)

@app.route('/users',methods=['POST'])
def create_user():

    new_username = request.json["username"]
    new_password = request.json["password"]

    if data["users"]:
        new_id = data["users"][-1]["id"] + 1
    else:
        new_id = 1

    new_user = {
        "id" : new_id,
        "username" : new_username,
        "password" : new_password,
        "details" : {
                "email":" ",
                "age": 0,
                "address": {
                    "city": " ",
                    "state": ""
                },
        },
        "orders" : []
    }

    data["users"].append(new_user)

    with open("json-files/data.json", "w") as file:
        json.dump(data, file, indent = 4)

    return jsonify({"message": "User created successfully", "user": new_user})

@app.route('/check',methods=['POST'])
def check_user():
    new_username = request.json["username"]
    new_password = request.json["password"]
    for user in data["users"]:
        if new_username != user["username"]:
            return jsonify("There is no such user")
        if new_password != user["password"]:
            return jsonify("password is incorrect")
            
        

# def create_user(data,new_username, new_password, age):
#     if data["users"]:
#         new_id = data["users"][-1]["id"] + 1
#     else:
#         new_id = 1
#     new_user = {
#         "id":new_id,
#         "username":new_username,
#         "password":new_password,
#         "details":{"age":age},
#         "orders":[]
#     }
#     data["users"].append(new_user)
#     print(f"user-id: {new_id},user-name: {new_username}, new-password: {new_password}, age: {age} ")

# create_user(data, "soham", "ghugare", 21)




if __name__ == '__main__':
     app.run(debug=True)