# Write a program that receives two numbers (factor and count). 
# It should create a list with a length of the given count that contains only integer numbers, which are multiples of the given factor. The numbers should be only positive, and they should be arranged in ascending order, starting from the value of the factor.

n_factor = int(input())
n_count = int(input())

multiples = []

for i in range(1,n_count+1):
    multiples.append(n_factor*i)

print(multiples)
