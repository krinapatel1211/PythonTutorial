derek_dict = {"f_name": "Derek", "l_name": "Banas", "address": "123 Main St"}

print("First Name: ", derek_dict["f_name"])
derek_dict["address"] = "215 North St"
print("New Address: ", derek_dict["address"])
derek_dict["city"] = "Pittsburgh"
print("Is there a city: ", "city" in derek_dict)
del derek_dict["f_name"]
for i, j in derek_dict.items():
    print(i, j)


