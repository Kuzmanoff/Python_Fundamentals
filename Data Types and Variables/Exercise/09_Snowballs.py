# Tony and Andi love playing in the snow and having snowball fights, but they always argue about who makes the best snowballs. 
# They have decided to involve you in their fray by writing a program that calculates snowball data and outputs the best snowball value.

# You will receive N – an integer, the number of snowballs being made by Tony and Andi. 
# On the following lines, you will receive 3 inputs for each snowball:
# · The weight of the snowball (integer).
# · The time needed for the snowball to get to its target (integer).
# · The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball


n = int(input()) # the number of snowballs
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for snowball in range(n):
    
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality

    if snowball_value > max_value:
        max_value = snowball_value
        max_weight = snowball_weight
        max_time = snowball_time
        max_quality = snowball_quality

print(f"{max_weight} : {max_time} = {max_value:.0f} ({max_quality})")
