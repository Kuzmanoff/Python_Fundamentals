# Write a program that receives a sequence of numbers, separated by a single space, 
# and prints their absolute value as a list. Use abs(). 

nums = input().split()

abs_values = []

for num in nums:
    abs_values.append(abs(float(num)))

print(abs_values)