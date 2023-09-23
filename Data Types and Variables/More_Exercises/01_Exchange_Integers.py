# Read two integer numbers and, after that, exchange their values.
# Print the variable values before and after the exchange, as shown below:

# Examples
# 5 10 
# Before: a = 5 b = 10 
# After: a = 10 b = 5

# 10 20 
# Before: a = 10 b = 20 
# After: a = 20 b = 10

a = int(input())
b = int(input())

print("Before:")
print(f"a = {a}")
print(f"b = {b}")

a2 = b
b2 = a

print("After:")
print(f"a = {a2}")
print(f"b = {b2}")
