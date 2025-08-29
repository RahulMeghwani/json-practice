import json

with open("json-files/data.json","r") as file:
    data = json.load(file)

# ## print(data)
# ##print(data["users"])
# # print(data["users"][0]["username"])
# # print(data["users"][1]["details"]["email"])
# # print(data["users"][0]["details"]["address"]["city"])
# # print(data["users"][0]["orders"][0]["item"])
# # print(data["users"]["orders"])
# # print(data["users"]["orders"])


# # for user in data["users"]:
# #     # if(data["users"]["orders"]["item"]) == "Mouse" :
# #     #     print(["users"]["username"])
# #     # print(user["orders"][0])
# #     for order in user["orders"]:
# #         ##print(order)
# #         ##print(order["item"])
# #         if (order["item"]) == "Mouse":
# #             print(user["username"])


# # for user in data["users"]:
# #     #print(user)
# #     #print(user["details"]["age"])
# #     if (user["details"]["age"]) > 21:
# #         #print(user["details"]) 
# #         print(user["username"])
# #         print(user["details"]["address"]["city"])
# #         print(len(user["orders"]))
# #     # for detail in user["details"]:
# #     #     #print("yes")
#     #     pass







# #Print the usernames of all users who ordered a “Phone”

# for user in data["users"]:
#     for order in user["orders"]:
#         if (order["item"]) == "Phone":
#             print(user["username"])


# # # Print the username and email of all users who live in "Delhi"

# for user in data["users"]:
#     if (user["details"]["address"]["city"]) == "Delhi":
#         print(user["username"])
#         print(user["details"]["email"])

# #Print the username and city of users who are older than 22.

# for user in data["users"]:
#     if(user["details"]["age"]) > 22:
#         print(user["username"])
#         print(user["details"]["address"]["city"])


# # Find all users who ordered an item worth more than 10,000 and print their username.

# for user in data["users"]:
#     for order in user["orders"]:
#         if (order["price"]) >= 10000:
#             print(user["username"])

# # 	Print the names of all items ordered by Rahul.

# for user in data["users"]:
#         if user["username"] == "rahul":
#             for order in user["orders"]:
#                 print(order["item"])

# # Print the username of the user who spent the most money.

# max_price = 0 
# for user in data["users"]:
#     for order in user["orders"]:
#         if (order["price"]) > max_price:
#             max_price = order['price']
# print("Maximum price:", max_price)


# #Print the order_id of all orders placed by Meghwani.

# for user in data["users"]:
#     if(user["username"]) == "meghwani":
#         for order in user["orders"]:
#             print(order["order_id"])


# # Find and print the city names of all users who bought a “Laptop”.

# for user in data["users"]:
#     for order in user["orders"]:
#         if(order["item"]) == "Laptop":
#             print(user["details"]["address"]["city"])



# # # Count how many users are older than 23.

# count = 0
# for user in data["users"]:
#     if(user["details"]["age"]) > 23:
#         count+=1
# print("The number of people greater than 23 is: ", count)



# # Print all unique items that have been ordered across all users.

# unique_items = set() 
# for user in data["users"]:
#     for order in user["orders"]:
#         unique_items.add(order["item"])
# print("Unique items:", unique_items)



# # Print the username and item of every order above ₹5000.

# for user in data["users"]:
#     for order in user["orders"]:
#         if (order["price"]) > 5000:
#             print(order["item"])
#             print(user["username"])


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


def update_user(data, id):
    for user in data["users"]:
        if(user["id"]) == id:
            # print(user["orders"])
            dummy_order = {"order_id": 105, "item": "Keyboard", "price": 40000}
            # user["username"] = "Hell"
            user["orders"].append(dummy_order)
    print(data)
    with open("json-files/data.json", "w") as f:
        json.dump(data, f, indent=4)


update_user(data, 2)