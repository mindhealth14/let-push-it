oldlist = ['Apple', 'Cherry', 'Banana']
oldlist.clear()
print(oldlist)

listdtype = ["abc", 24, True, 40, "Male"]


thislist =list(("Apple", "Mango", "Banana", "Orange"))

#print(type(thislist))

#print(thislist)


print(thislist[2:4])

thislist[1] = "Cashew"

print(thislist)

thelist = list(("Pear", "Kiwi", "Watermelon", "Blueberry"))
del thelist[2]

thislist.insert(0, "Watermelon")
print(thislist)

thislist.append(thelist)
print(thislist)


thislist.append('Blackberry')

print(thislist)

new = ['grape', 'strawberry', 'blackcurrants']
new.remove("grape")

thislist.extend(new)

print(thislist)

new.pop("strawberry")