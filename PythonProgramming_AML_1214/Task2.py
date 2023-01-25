import turtle

# 1. create a list to print 10 furniture stores items
list_furn_store = ["Furniture1", "Furniture2", "Furniture3", "Furniture4", "Furniture5", "Furniture6", "Furniture7",
                   "Furniture8", "Furniture9", "Furniture10"]

# 2. replace all of the items with gadgets
list_furn_store = ["Gadgets1", "Gadgets2", "Gadgets3", "Gadgets4", "Gadgets5", "Gadgets6", "Gadgets7", "Gadgets8",
                   "Gadgets9", "Gadgets10", ]

# 3. print the values using for loop
for i in range(len(list_furn_store)):
    print(list_furn_store[i])

# 4. sort the items in desecnding order
list_furn_store.reverse()
print(list_furn_store)

# 5. delete middle 2 items
list_furn_store.pop(5)
list_furn_store.pop(4)
print(list_furn_store)

# 6. craeet one more list for keeping college names in Ontario
list_college_names = ["Lambton", "Humber", "Seneca", "Conestoga"]

# 7. now merge both lists gadgets and college
merged_list = list_furn_store + list_college_names
print(merged_list)

# 8. draw following shapes
# 9. Draw a tree  of your choice with green color inside the tree
turtle.pencolor('black')
turtle.pensize(5)
turtle.fillcolor('green')
turtle.begin_fill()
turtle.goto(50, 0)
turtle.goto(-50, 0)
turtle.goto(0,100)
turtle.goto(50, 0)

turtle.goto(0, 0)
turtle.goto(-100, -100)
turtle.goto(100, -100)
turtle.goto(0, 0)

turtle.goto(-100, -100)
turtle.goto(0, -100)
turtle.goto(-200, -200)
turtle.goto(200, -200)
turtle.goto(0, -100)
turtle.end_fill()

turtle.goto(-200, -200)
turtle.goto(-30, -200)
turtle.begin_fill()
turtle.fillcolor("brown")
turtle.goto(-30, -280)
turtle.goto(30, -280)
turtle.goto(30, -200)
turtle.end_fill()

turtle.done()





