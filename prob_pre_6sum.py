import prob_preflop
import random

player = []
p_num = 6
p_list = []
for i in range(p_num):
    p_list.append([])
    p_list[i].append(0)
    p_list[i].append(0)

def prob2():
    p_list2 = []
    for i in range(p_num):
        p_list2.append([])
    for i in p_list2:
        c1 = random.randint(prob_preflop.f,prob_preflop.l)
        c2 = random.randint(prob_preflop.f, prob_preflop.l)
        mn = min(c1,c2)
        mx = max(c1,c2)
        i.append(mx)
        i.append(mn)
    return p_list2

def sort_plist(pl):
    pl1 = sorted(pl,key=lambda x: sum(x))
    return pl1

print(sort_plist(prob2()))
r=100

for i in range(r):
    p=prob2()
    p=sort_plist(p)
    for ii in range(len(p)):
        p_list[ii][0]+=p[ii][0]
        p_list[ii][1] += p[ii][1]
for i in p_list:
    print(i[0]/r,i[1]/r, (i[0]+i[1])/2/r)
