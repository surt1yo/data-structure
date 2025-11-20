#Create a list of square values of numbers between specified ranges by the user, 
#and then separate the odd and even values.
start=int(input("Enter start of range: "))
end=int(input("Enter end of range: "))
square=[x ** 2 for x in range(start, end + 1)]
even_squares=[sq for sq in square if sq % 2 == 0]
odd_squares=[sq for sq in square if sq % 2 != 0]
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)
