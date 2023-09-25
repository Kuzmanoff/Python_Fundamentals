# You will be given number n. After that, you'll receive different strings n times. Your task is to check if the given strings are pure, meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore "_":

# · If a string is pure, print "{string} is pure."

# · Otherwise, print "{string} is not pure!" 

number_of_string = int(input())

for current_string in range(number_of_string):
    pure_or_not_pure_string = input()
    if "," in pure_or_not_pure_string or \
            "." in pure_or_not_pure_string or \
            "_" in pure_or_not_pure_string:
        print(f"{pure_or_not_pure_string} is not pure!")
    else:
        print(f"{pure_or_not_pure_string} is pure.")