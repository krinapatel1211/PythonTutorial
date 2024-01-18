
def enter_customer_details(cust_dict1):
    f_name, l_name = input("Enter Customer Name: ").split()
    cust_dict1.append({"f_name": f_name, "l_name": l_name})


cust_dict = []
while True:
    customer_exists = input("Enter Customer (y/n) : ")
    if customer_exists == "y":
        enter_customer_details(cust_dict)
    else:
        break

for cust in cust_dict:
    print(cust['f_name'], cust['l_name'])
