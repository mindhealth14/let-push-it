thislist = ['Apple', 'Cherry', 'Banana']

##print(thislist)

#print(len(thislist))

listdtype = ["abc", 24, True, 40, "Male"]
#print(listdtype)

#print(type(listdtype))

# List constructor 

thislist =list(("Apple", "Mango", "Banana", "Orange"))

#print(type(thislist))

#print(thislist)


print(thislist[2:4])

thislist[1] = "Cashew"

print(thislist)

thelist = list(("Pear", "Kiwi", "Watermelon", "Blueberry"))

thislist.insert(0, "Watermelon")
print(thislist)

thislist.append(thelist)
print(thislist)


thislist.append('Blackberry')
print(thislist)

new = ['grage', 'strawberry', 'blackcurrent']

thislist.extend(new)

print(thislist)