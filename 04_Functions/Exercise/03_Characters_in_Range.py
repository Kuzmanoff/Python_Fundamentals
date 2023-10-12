def all_char(first, second) -> list:
    chars = []
    for curr_char in range(ord(first)+1, ord(second)):
        chars.append(chr(curr_char))
    return chars
    

char1 = input()
char2 = input()
final_result = all_char(char1,char2)

print(" ".join(final_result))