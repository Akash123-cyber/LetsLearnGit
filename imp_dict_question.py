seq=[int(x) for x in input("enter the numbers: ").split()]

# example how the dictionary should form
# d={1:2,2:2,3:1,5:1}

def frequency(seq):
    seq.sort()
    l1=[]
    for i in seq:
        if i not in l1:
            l1.append(i)
    
    c=[]
    for i in l1:
        count=0
        for j in seq:
            if i==j:
                count+=1
        c.append(count)

    d=dict(zip(l1,c))

    l2=[]
    lmax=[]
    lmin=[]
    for i in d.keys():
        if d[i]==max(d.values()):
            lmax.append(i)
        elif d[i]==min(d.values()):
            lmin.append(i)
    l2.append(lmin)
    l2.append(lmax)
    l2.append(min(d.values()))
    l2.append(max(d.values()))
    print(tuple(l2))

frequency(seq)