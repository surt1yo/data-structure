#Write a Python program to count the number 
#of strings where the string length is two or more, 
#and the first and last characters are the same from a given list of strings.
str_list=['abc', 'cfc','xyz', 'aba', '1221']
length=len(str_list)
for i in str_list:
    word=i
    if len(word)>=2 and word[0]==word[-1]:
        print(word)