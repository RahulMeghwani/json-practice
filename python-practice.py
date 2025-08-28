import json

with open("json-files/data.json","r") as file:
    data = json.load(file)

## print(data)
##print(data["users"])
# print(data["users"][0]["username"])
# print(data["users"][1]["details"]["email"])
# print(data["users"][0]["details"]["address"]["city"])
# print(data["users"][0]["orders"][0]["item"])
# print(data["users"]["orders"])
# print(data["users"]["orders"])


# for user in data["users"]:
#     # if(data["users"]["orders"]["item"]) == "Mouse" :
#     #     print(["users"]["username"])
#     # print(user["orders"][0])
#     for order in user["orders"]:
#         ##print(order)
#         ##print(order["item"])
#         if (order["item"]) == "Mouse":
#             print(user["username"])


for user in data["users"]:
    #print(user)
    #print(user["details"]["age"])
    if (user["details"]["age"]) > 21:
        #print(user["details"]) 
        print(user["username"])
        print(user["details"]["address"]["city"])
        print(len(user["orders"]))
    # for detail in user["details"]:
    #     #print("yes")
    #     pass