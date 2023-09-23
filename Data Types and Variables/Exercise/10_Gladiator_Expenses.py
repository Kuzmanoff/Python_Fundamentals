# As a gladiator, Peter needs to repair his broken equipment when he loses a fight. 
# His equipment consists of a helmet, a sword, a shield, and an armor.
# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment.

# Input / Constraints
# The input will consist of 5 lines:
# · On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
# · On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000].
# · On the third line, you will receive the sword price - a floating-point number in the range [0, 1000].
# · On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000].
# · On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000].

# Output
# · As output, you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"

loss_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_broken = False
sword_broken = False

helmet_break_counter = 0
sword_break_counter = 0
shield_break_counter = 0
armor_break_counter = 0

total_expenses = 0 

for loss in range(1,loss_count+1):

    if loss % 2 == 0:
        helmet_broken = True
        helmet_break_counter += 1
    else:
        helmet_broken = False

    if loss % 3 == 0:
        sword_broken = True
        sword_break_counter += 1
    else:
        sword_broken = False

    if sword_broken and helmet_broken:
        
        shield_break_counter += 1
        
        if shield_break_counter % 2 == 0:
        
            armor_break_counter += 1

    
total_expenses = (helmet_break_counter * helmet_price) + (sword_break_counter * sword_price) + (shield_break_counter* shield_price) + (armor_break_counter*armor_price)

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
