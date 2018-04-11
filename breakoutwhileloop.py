import random

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

print("Enemy strikes for" , dmg ,"Points of damage. current Hp is", playerhp )

