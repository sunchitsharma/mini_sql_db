def intersection(l1,l2):
    l3=[]
    for i in l1:
        if i not in l3:
            l3.append(i)

    for i in l2:
        if i not in l3:
            l3.append(i)

    return l3


def union(l1,l2):
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)

    return l3
