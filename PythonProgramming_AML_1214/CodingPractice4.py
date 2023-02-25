guest_list = ["Deep", "Neel", "Parth", "Nirjari"]

print("***Here is the invitations***")
for i in guest_list:
    print("{}-There is a dinner party at my home. I cordially invite {} to this"
          " party".format(i, i))

# a = input("\nEnter the name of the guest who can't come: ")
# guest_list.remove(a)
guest_list.remove("Neel")
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

new_list = guest_list.copy()
print("\nFound a small dinner table now, can only invite 2 people!")
print(len(new_list))
for i in new_list:
    new_list.pop()
    print(new_list)
    print("Sorry {}, I can't invite you for dinner!".format(i))

print()
for i in new_list:
    print("{}- There is a dinner party at my home. I cordially invite {} to this"
          " party".format(i, i))






