from str2card import r_card,cards,split_to_pairs
from preflop import preflop

while(True):
    i = input("preflop: ")
    preflop(i)
    i1 = split_to_pairs(i)

    print("preflop: ", i)