import random

a3 = True # این مورد دقیقا در صورت سوال اومده 

a1 = random.choice([True, False])
c3 = not a1

a2 = True # اگر این مورد را رندوم بزاریم ممکن است غلط  باشد که این باعث بهم ریختن تعداد درست و غلط ها میشود(درست؛۷ و غلط : ۵ )
b3 = not a2
c2 = b3 

b1 = random.choice([True, False])
d1 = not b1

b2 = random.choice([True, False])
d3 = not b2

c3 = random.choice([True, False])
d2 = not c3

for i in range(0, 1):
    if a2 == True:
        print('the answer is b')
    elif b1 == False:
        print("the answer is d")
    elif b2 == False:
        print("the answer is a")
    else:
        print('the answer is c')

