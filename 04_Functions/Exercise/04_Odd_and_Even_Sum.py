def sum_of_even_and_odd_digits(number):
    even_sum = 0
    odd_sum = 0

    for digit in str(number):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    result = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return result


number = int(input())


result = sum_of_even_and_odd_digits(number)
print(result)