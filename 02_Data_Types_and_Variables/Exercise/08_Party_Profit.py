# As a young adventurer, you travel with your group worldwide, seeking for gold and glory. 
# But you need to split the profit among your companions.
# You will receive a group size. After that, you receive the days of the adventure.
# Every day, you earn 50 coins, but you also spend 2 coins per companion for food.
# Every 3rd (third) day, you organize a motivational party, spending 3 coins per companion for drinking water.
# Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion. 
#   But if you have a motivational party the same day, you spend additional 2 coins per companion.
# Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave, 
#   but every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.

You should calculate how many coins gets each companion at the end of the adventure
group = int(input())
days = int(input())

coins = 0
party = False

for day in range(1,days+1):
    coins += 50
   
    if day % 10 == 0:
        group -= 2
    if day % 15 == 0:
        group += 5

    coins -= group * 2

    if day % 3 == 0:
        coins -= group * 3
        party = True
    else:
        party = False
    if day % 5 == 0:
        coins += group * 20
        if party:
            coins -= group * 2

coin_split = coins//group #floor(coins/group)

print(f"{group} companions received {coin_split} coins each.")
