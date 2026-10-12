# CONCEPT - 1: Creating and accessing JSON data

import json


#==================================================================
data = {'name':'sreeyutha','age': '24','job':'AI Eng'}

text = json.dumps(data)

result = json.loads(text)

print(result)

print("The name of the person is:", result['name'])
print("The age of the person is:", result['age'])
print("The job of the person is:", result['job'])

#==================================================================
product = {
    "id": 101,
    "name": "Laptop",
    "price": 55000,
    "in_stock": True
}
# print("json.dumps:", text)
# print("json.loads:", result)
text2 = json.dumps(product)
result2 = json.loads(text2)

print(result2)

print("The ID of the product is:", result2['id'])
print("The name of the product is:", result2['name'])
print("The price of the product is:", result2['price'])
print("Is the product in stock?", result2['in_stock'])
