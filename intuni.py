try:
    def union(l1,l2):
        l3=[]
        for i in l1:
            if i not in l3:
                l3.append(i)

        for i in l2:
            if i not in l3:
                l3.append(i)

        return l3


    def intersection(l1,l2):
        l3=[]
        for i in l1:
            if i in l2:
                l3.append(i)

        return l3
except:
    "Error Occured in and or condition"

############ TEST CODE #############

# print intersection([1,2,3,4],[1,2,5])
# print union([[1,3],[1,2]],[[1,2],[3,4]])

#####################################
