

import random



random_number = random.randint(0,10)
while(True):
    inp = int(input("please enter a value between 0 -10 "))
    if(random_number== inp):
        print("You are correct!!! ",random_number)
        break
    else:
        print("Better luck next time!!!")