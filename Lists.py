
# define list
places_to_see = ["New Zealand","Iceland","Thailand","Vietnam","Sri Lanka"]

print("-------------------------------------------")

# print list to terminal
print("\nObjective 1 - Print the List in RAW form")
print(places_to_see)

# print sorted list to terminal
print("\n\nObjective 2 - Print the List in sorted form, without altering the list")
print(sorted(places_to_see))
#print(str(sorted(places_to_see)) + "\n\n")

# reprint list to prove using sorted did not change the list
print("\nObjective 3 - Print the list again to show that previous operation did not alter the list")
print(places_to_see)

# Reverse list items order
print("\nObjective 4 - Reverse the order of the items in the list, re print list to show that items are now stored in reverse order")
places_to_see.reverse()
print(places_to_see)

# reverse list back
print("\nObjective 5 - Use the reverse funtion to change the order of the items in the list back again, print to confirm")
places_to_see.reverse()
print(places_to_see)

# sort list and change its stored order
print("\nObjective 6 - Use the sort function to change the order of the list so that it is in alphabetical order")
places_to_see.sort()
print(places_to_see)

# sort list items in reverse alphabetical order
print("\nObjective 7 - Use the sort function to change the order of the list so that it is in reverse alphabetical order")
places_to_see.sort(reverse=True)
print(places_to_see)


# Insert new location into the list
print("\nObjective 8 - Insert new Location into the list, Bristol should be inserted into position '0' in the list ")
places_to_see.insert(0, 'Bristol')
print(places_to_see)

# Insert new location into the list, using the append function.  Useful as you may not know the length of the list - this adds and item to the end of the list
places_to_see.append('Dublin')
print ("\nObjective 9 - Append a new location to the end of the list using the append function")
print("List with new location 'Dublin' added:" + " " + str(places_to_see))

# Remove Item from list using del
print("\nObjective 10 - Remove item from list , using Del function - Bristol will be removed from list")
del places_to_see[0]
print(places_to_see)


# Remove item from list using pop(n) - used when you need to use an item and want to simultaneously remove the item from the original list
print("\nObjective 11 - Remove item from list , using pop() function.  Remove list item 2 from list whilst simultaneously assigning it to a variable")
places_to_see_Popped = places_to_see.pop(2)
print("\n\tPopped location:" + str(places_to_see_Popped))

print("\n\tOriginal List:" + str(places_to_see))