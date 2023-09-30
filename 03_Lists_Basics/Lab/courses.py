# On the first line, you will receive a single number n. 
# On the following n lines, you will receive names of courses. You should create a list of courses and print it.

n = int(input())
course_list = []

for _ in range(n):
    course = input()    
    course_list.append(course)

print(course_list)