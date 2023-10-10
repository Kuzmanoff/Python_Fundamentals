# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it. Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers. 
# The operator can be one of the following: "multiply", "divide", "add", "subtract".

def calculate_result(operator, num1, num2):
    if operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        return int(num1 / num2)
    elif operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2

operator = input()
num1 = int(input())
num2 = int(input())
result = calculate_result(operator,num1,num2)
print(result)