from gen_card_deck import card_deck
import random
f=2
l=14

def av():
    return random.randint(f,l)

def fir():
    f1 = max(random.randint(f,l),random.randint(f,l))
    return f1

def sec():
    f1 = min(random.randint(f,l),random.randint(f,l))
    return f1


def prob1():
    r = 10000
    a = 0
    f1 = 0
    s = 0
    for x in range(r):

        a+=av()
        f1+=fir()
        s+=sec()
        # print(a/r,f/r,s/r)
    return a,f1,s,r

for i in range(10):
    a,f1,s,r = prob1()
    print(a / r, f1 / r, s / r)