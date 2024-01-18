"""
r - read --> Display the content
a - append --> To add more content
w - writing --> Replace the old content with the new content

"""

obj = open('StudentTextFile', 'r')
print(obj.read())
obj.close()

# appending and reading from file
obj = open('StudentTextFile', 'a')
obj.write("\nI have added this text with append!")
obj.close()

obj = open('StudentTextFile', 'r')
print(obj.read())
obj.close()

# replacing the old content with the new one
obj = open('StudentTextFile', 'w')

obj.close()
