import math
import random

#a = random.randrange(0,9)
#b = random.randint(0,9)

def whileloop(x,y):
    x = x
    while x != y:
        x = random.randint(0,9)
        print(x)

def seeder():
    random.seed(12)
    print(random.random())
    random.seed(12)
    print(random.random())


def checker():
    #print(str(random.randint(0,1)) + str(random.randint(0,1)), end='')
    #print(random.randrange(0,1))
    #print(random.randrange(0,20,5))
    #name = 'Yoon'
    #print(random.choice(name))
    teachers = ('Pak', 'Kim', 'Yoon')
    print(random.sample(teachers,3))

def random_seed(s):
    s = random.seed(s)
    return random.random()

s = float(input("Enter a value: "))
print(random_seed(s))







#checker()
#seeder()
#whileloop(1,7)