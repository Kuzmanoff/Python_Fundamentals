# You will be given two strings. Transform the first string into the second one, letter by letter, starting from the first one. After each interaction, print the resulting string only if it is unique.

# Note: the strings will have the same length. 

str_1 = input()
str_2 = input()
last_str = str_1

for char in range(len(str_1)):
    left_part = str_2[:char+1]
    right_part = str_1[char+1:]
    new_string = left_part + right_part

    if new_string != last_str:
        print(new_string)
        last_str = new_string