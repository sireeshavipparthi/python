# continue breakout loops
import random

p1 = 260
etkl = 60
etkh = 80

while p1 > 0:
  dmg = random.randrange(etkl, etkh)
  p1 = p1 - dmg

  if p1 <= 30:
     p1 = 30

  print("Enemy strikes for" , dmg ,"Points of damage. current HP is", p1)

  if p1 == 30:
   continue
   print("you have low health. you've been reported to the nearest inn.")
  break
