r_card = {
    "t" : 10,
    "j" : 11,
    "q" : 12,
    "k" : 13,
    "a" : 14
}
def get_key_by_value(d, target_value):
    for key, value in d.items():
        if value == target_value:
            return key
    return None
def split_to_pairs(s):
    return [s[i:i+2] for i in range(0, len(s), 2)]

def cards(pair):
    if pair[0] in r_card:
        a = r_card[pair[0]]
    else :
        a = int(pair[0])
    b = pair[1]
    return a,b