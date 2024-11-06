from gen_card_deck import card_deck
import random


def count1(hand,target, card_num):
    g = []
    for i in range(0,card_num):
        c = 1
        while(c):
            r = random.choice(card_deck)
            # print(r,hand)
            if r in hand:
                continue
            c = 0
            hand.append(r)
            g.append(r)

    for i in target:
        if i in g:
            return 1
    return 0

def prob_triple():
    hand = ["a0","a1"]
    target = ["a2","a3"]
    card_num = 3
    r = 1000000
    p = 0
    print(range(0,r))
    for i in range(0,r):
        hand = ["a0", "a1"]
        target = ["a2", "a3"]
        # print(card_deck)
        # print(i)
        p += count1(hand,target,card_num)
    print("triple flop",p/r)
    card_num = 5
    for i in range(0,r):
        hand = ["a0", "a1"]
        target = ["a2", "a3"]
        # print(card_deck)
        # print(i)
        p += count1(hand,target,card_num)
    print("triple river",p/r)

prob_triple()