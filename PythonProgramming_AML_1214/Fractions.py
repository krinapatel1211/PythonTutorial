from fractions import Fraction

print(Fraction(2, 3))

names = ['Krina','Deep','Neel','Vidhi']
age = [20,22,23,24]
print("Name  Age")
print(names[0],'=',age[0])
print(names[1],'=',age[1])

names.remove("Krina")
print(names)
names.pop(2)
print(names)
names.append("Krina")
print(names)
print(names.count("Krina"))
print(names.index("Krina"))
print(names.insert(1, "Vidhi"))
print(names)
print(names.reverse())
print(names)
print(names.sort())
print(names)
print(len(names))
new_list = names + age
print(new_list)


