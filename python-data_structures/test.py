Name = ["Apple", "Mango", "Pineapple", "Guava", "Orange"]

People = ["Mary", "Sophia", "Paul", "Grace"]
#Append- By default it takes the element to the last index

Name.append(20)
#Insert- By inserting you specify the location where you need
# to put your element by adding the index, and the element.

Name.insert(2, "Pawpaw")
#Extend= By adding list to our list

Name.extend([2, 4,7])
#Remove- You use remove by specifying the item or element you want to remove
Name.remove("Mango")

#pop- It removes the item or element with an index, and returns it.
# If no index is specified, it removes the last element
Name.pop(4)

#clear- It removes all the items or elements in the list
People.clear()

#Reverse- It changes the position in the list from back to front
Name.reverse() or Name[::-1]
#Repetition- Repeat the items in the list the number of times you want.
print(Name * 3)
