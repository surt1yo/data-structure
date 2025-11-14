#Write a Python program to find the sum and average of the list. 
#The average of the list is defined as the sum of the elements divided by the number of the elements.
#Also, find the largest and the smallest number in the list.
num_list=[984,976,184,323,975]
sum=0
for i in num_list:
    sum=sum+i
    
print(sum)
avg=sum/len(num_list)
print(avg)
num_list.sort()
print(num_list)
print("Smallest number:", num_list[0])
print("Largest number: ", num_list[-1])