# Write a program that receives a single string containing positive and negative numbers 
# separated by a single space. 
# Print a list containing the opposite of each number.

numbers_str = input()

numbers = numbers_str.split()

opposites = [] 

for number in numbers:
    number = -int(number)
    opposites.append(number)

print(opposites)
