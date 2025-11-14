#Write a program to perform the following operations on a List:
#1. Create an empty list
#2. A list with elements
#3. Use * operator 
#4. Reverse a list
empty_list = []
list_with_elements=[1,2,3,4,5]
print("Empty List:", empty_list)
print("List with elements:", list_with_elements)
multiply_list = list_with_elements * 3
print("Multiplied List:", multiply_list)
reversed_list = list_with_elements[::-2]
print("Reversed List:", reversed_list)