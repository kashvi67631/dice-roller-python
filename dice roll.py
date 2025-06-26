#dice
print("Thank You For choosing us let's roll the dice")
import random
while True:
        print('the dice number is',random.randrange(1,7))
        ch=input('Do you want to enter more?:yes/no')
        if ch.lower()=='no':
            break
