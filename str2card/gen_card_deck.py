from str2card import r_card,get_key_by_value

card_deck = []
for i in range(2, r_card["a"]+1):
    for ii in range(0,4):
        k=get_key_by_value(r_card,i)
        if(k):
            s = k+str(ii)
        else:
            s = str(i)+str(ii)
        # print(s)
        card_deck.append(s)
# print(card_deck, len(card_deck))