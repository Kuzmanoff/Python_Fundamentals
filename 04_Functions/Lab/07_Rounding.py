# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use round().
numbers_str = input()


numbers = numbers_str.split()


rounded_numbers = [round(float(num)) for num in numbers]


print(rounded_numbers)
