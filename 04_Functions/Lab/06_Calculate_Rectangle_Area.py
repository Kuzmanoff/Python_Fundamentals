# Create a function that calculates and returns the area of a rectangle by given width and height. Print the result on the console.def calculate_rectangle_area(width, height):
    area = width * height
    return area

width = int(input())
height = int(input())

area = calculate_rectangle_area(width, height)

print(area)