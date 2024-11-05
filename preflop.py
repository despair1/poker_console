from str2card import r_card,cards,split_to_pairs

def not_pair(p):
    h, _ = cards(p[0])
    print("-High card: ", (r_card["a"] - h) * 4 / 52 * 100)
    print("-high pair: ", (r_card["a"] - h)  / 52 * 100)
def pair(p):
    h, _ = cards(p[0])
    print("-high pair: ", (r_card["a"] - h) / 52 * 100)
    print("+trips: ", (2/50+2/49+2/48)*100)

def preflop(pf):
    p = split_to_pairs(pf)
    if p[0][0] != p[1][0]:
        not_pair(p)
    else:
        pair(p)
