# You have a water tank with a capacity of 255 liters. 
# On the first line, you will receive n – the number of lines, which will follow. 
# On the following n lines, you will receive liters of water (integers), which you should pour into your tank
# If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. 
# On the last line, print the liters in the tank.

capacity = 255 #liters

n = int(input()) #number of lines, which will follow

total_liters = 0
total_capacity = 0

for liters in range(n):
    
    liters_of_water = int(input())
    total_capacity = capacity - total_liters

    if liters_of_water > total_capacity:
        print("Insufficient capacity!")
        continue
    total_liters += liters_of_water
    
print(total_liters)
