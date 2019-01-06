# Looking at Loops in Python
# for loops are in the following format
# for LOOP_VARIABLE in 


# Objective 1 - Use a 'for loop' to print the numbers 1 - 15, using the range() function
print("\nObjective 1 - Use 'for loop' to print numbers in range 1 - 15 using the range() function")
for number in range(1,16):
    print (number)


# Objective 2 - Use a 'for loop' in conjunction with the range() function to print a list of even numbers
print("\nObjective 2 - Use a 'for loop' in conjunction with the range() function to print a list of even numbers")
for number in range(1,20,2):
    print (number)

# Objective 3 - Use a 'for loop' in conjunction with the range() function to print a list of even numbers
print("\nObjective 3 - Use a 'for loop' in conjunction with the range() function to print a list of odd numbers")
for number in range(1,20,3):
    print (number)

# Objective 4 - Use a 'for loop' to print all values within a list in order
print("\nObjective 4 - Define a list with a number of items, using a 'for loop' step through the list printing one list item on each iteration throgh the loop")
test_list = ['Item 0', 'Item 1', 'Item 2', 'Item 3']
for loop_Variable in test_list:
    print (loop_Variable)



# Objective 5 - Use the sum(), min() and max() functions to expose list statitics
print("\nObjective 5 - Use the sum(), min() and max() functions to expose list statitics ")
Ranged_List_1 = list(range(1,1000000))
print("max number of items in list is as below;")
print(max(Ranged_List_1))
print("\nmin number of items in list as below;")
print(min(Ranged_List_1))
print("\nsum of all numbers in list (range 1- 1000000) listed below;")
sum(Ranged_List_1)
print(sum(Ranged_List_1))



# Objective 6 - Print a list of square numbers in the range of 1 - 10
print("\nObjective 6 - Print a list of square numbers in the range of 1 - 10")
for number in range (1,11):
    print(str(number) + " " + "squared = " + str(number**2))

