import filereader as fr
import metadata_reader as mr
import itertools
import sys


info = mr.metadata_reader()

################### FORMAT PRINT ###################

def format_print(answer):
    for i in answer:
        for j in i:
            if i[-1]!=j:
                sys.stdout.write(j+",")
            else:
                sys.stdout.write(j)
        print


#################### MAIN FUNCION ##################

def runquery(select_part,from_part,where_part):

    # TYPE 1 : Select all records
    if(str(select_part[0])=="*"):
        final_answer=starquery(from_part,where_part)
        format_print(final_answer)

    # TYPE 2 : AGGRIGATE FUNCTIONS
    if(str(select_part[0][0:3]).lower()=="max" or str(select_part[0][0:3]).lower()=="min" or str(select_part[0][0:3]).lower()=="sum" or str(select_part[0][0:7]).lower()=="average"):
        final_answer=aggquery(select_part,from_part)
        print final_answer


#################### TYPE 1 QUERIES #####################

def starquery(from_part,where_part):
    answer = []
    opentables = []
    for i in from_part:
        opentables.append(fr.filereader(i))

    for element in itertools.product(*opentables):
        answer.append(element)

    final_answer=[]
    count =-1;
    for i in answer:
        temp = []
        for j in i:
            temp.extend(j)
        final_answer.append(temp)

    return final_answer

################### END OF TYPE 1 QUERIES ################

##################### TYPE 2 QUERIES #####################

def aggquery(select_part,from_part):

    opentables = []
    # FETCHING THE TABLE
    for i in from_part:
        opentables.append(fr.filereader(i))

    # FETCHING AGGRIGATION INDEX
    st = select_part[0].index("(")
    en = select_part[0].index(")")
    index = info[from_part[0]].index(select_part[0][st+1:en:1])

    # FOR MAX
    if(str(select_part[0][0:3]).lower()=="max"):
        max = int(opentables[0][0][index])
        for i in opentables[0]:
            if int(i[index])>max:
                max = int(i[index])
        return max

    # FOR MIN
    if(str(select_part[0][0:3]).lower()=="min"):
        min = int(opentables[0][0][index])
        for i in opentables[0]:
            if int(i[index])<min:
                min = int(i[index])
        return min

    # FOR SUM
    if(str(select_part[0][0:3]).lower()=="sum"):
        sum = 0
        for i in opentables[0]:
            sum+= int(i[index])
        return sum

    # FOR AVERAGE
    if(str(select_part[0][0:7]).lower()=="average"):
        sum = 0
        for i in opentables[0]:
            sum+= int(i[index])
        return sum/len(opentables[0])

############## END OF AGGRIGATE QUERIES ##################
