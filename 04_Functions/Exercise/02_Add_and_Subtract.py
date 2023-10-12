def sum_num(first,second):
    return first + second

def subtract(result,third):
    return result - third

def add_and_subtract(first,second, third):
    returned_result = sum_num(first,second)
    final_result = subtract(returned_result, n3)
    return final_result

n1 = int(input())
n2 = int(input())
n3 = int(input())

print(add_and_subtract(n1,n2,n3))