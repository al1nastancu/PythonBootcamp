# Flip the coin
import random

print("Let's flip some coins today!")
# 1 - means Heads
# 0 - means Tails

coin = random.randint(0,1)
print(coin)

if coin == 1:
    print("Heads")
else:
    print("Tails")