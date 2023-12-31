# On the first line, you will receive a number n. 
# On the second line, you will receive a word. 
# On the following n lines, you will be given some strings. 
# You should add them to a list and print them. 
# After that, you should filter out only the strings that include the given word and print that list too.

n = int(input())
magic_word = input()

strings = []

for _ in range(n):
    string = input()
    strings.append(string)

print(strings)

filtered_strings = []

for current_string in strings:
    if magic_word in current_string:
        filtered_strings.append(current_string)

print(filtered_strings)