dict1 = {"brand": "Toyota", "model": "Raw4", "year": 2023}

print(dict1.keys())
print(dict1.values())

a = dict1["brand"]
print(a)

b = dict1["year"]
print(b)

dict1["year"] = 2022
print(dict1["year"])

dict1["color"] = "red"
print(dict1)

dict1.pop("model")
print(dict1)

for i in dict1:
    print(dict1[i])

new_dict1 = dict1.copy()
print(new_dict1)

new_dict_equal = dict1
new_dict_equal["year"] = 2023
print(dict1["year"])
