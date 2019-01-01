
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


