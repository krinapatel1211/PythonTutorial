guest_list = ["Deep", "Neel", "Parth", "Nirjari"]

print("***Here is the invitations***")
for i in guest_list:
    print("{}-There is a dinner party at my home. I cordially invite {} to this"
          " party".format(i, i))

a = input("\nEnter the name of the guest who can't come: ")
guest_list.remove(a)
print("\n***Here is the modified invitations***")
for i in guest_list:
    print("{}- There is a dinner party at my home. I cordially invite {} to this"
          " party".format(i, i))

print("\nI have found a bigger dinner table, hence require 3 more guests\n")
guest_list.insert(0, "Smit")
guest_list.insert(2, "Shanky")
guest_list.append("Shivani")

for i in guest_list:
    print("{}- There is a dinner party at my home. I cordially invite {} to this"
          " party".format(i, i))

print("\nFound a small dinner table now, can only invite 2 people!")
print("People invited: ", len(guest_list))

while True :
    if len(guest_list) <= 2:
        print()
        break
    else:
        guest_list.pop()
        print("Sorry, I can't invite you for dinner!")


for i in guest_list:
    print("{}- There is a dinner party at my home. I cordially invite {} to this"
          " party".format(i, i))

print("People invited: ", len(guest_list))
del guest_list[0:2]
print("\nEmpty List :", guest_list)
print("People invited: ", len(guest_list))
