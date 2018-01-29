import filereader as fr
import metadata_reader as mr
import itertools
import sys
import numpy as np


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
        answer_names,final_answer=starquery(from_part,where_part)
        for j in answer_names:
            if answer_names[-1]!=j:
                sys.stdout.write(str(j)+",")
            else:
                sys.stdout.write(str(j))
        print

        format_print(final_answer)

    # TYPE 2 : AGGRIGATE FUNCTIONS
    elif(str(select_part[0][0:3]).lower()=="max" or str(select_part[0][0:3]).lower()=="min" or str(select_part[0][0:3]).lower()=="sum" or str(select_part[0][0:7]).lower()=="average"):
        final_answer=aggquery(select_part,from_part)
        print final_answer

    # TYPE 3 : PROJECTION QUERIES
    elif(str(select_part[0])!="*" and str(select_part[0]).lower()!="distinct"):
        answer_names,final_answer=starquery(from_part,where_part)
        return_answer=projection(select_part,from_part,answer_names,final_answer)

        for i in return_answer:
            for j in i:
                if j != i[-1]:
                    sys.stdout.write(str(j)+",")
                else:
                    sys.stdout.write(str(j))
            print


    # TYPE 4 : DISTINCT QUERIES
    elif(str(select_part[0]).lower()=="distinct"):
        answer_names,final_answer=starquery(from_part,where_part)
        return_answer=projection(select_part,from_part,answer_names,final_answer)
        return_answer=distinct_handler(answer_names,return_answer)

        for i in return_answer:
            for j in i:
                if j != i[-1]:
                    sys.stdout.write(str(j)+",")
                else:
                    sys.stdout.write(str(j))
            print



#################### TYPE 1 QUERIES #####################

def starquery(from_part,where_part):
    answer = []
    opentables = []
    answer_names=[]

    for i in from_part:
        opentables.append(fr.filereader(i))
        for j in info[i]:
            answer_names.append(i+"."+j)

    for element in itertools.product(*opentables):
        answer.append(element)

    final_answer=[]
    count =-1;
    for i in answer:
        temp = []
        for j in i:
            temp.extend(j)
        final_answer.append(temp)

    return answer_names,final_answer

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

#################### TYPE 3 QUERIES ######################

def projection(select_part,from_part,answer_names,final_answer):
    indexes=[]

    # FOR TYPE OF NAMES : table_name.colname

    if(len(from_part)>1): # WORKING CORRECTLY
        for i in select_part:
            if(i!="distinct"):
                indexes.append(answer_names.index(i))

    #FOR TYPE OF NAMES : table.colname
    else:
        if(select_part[0]!="distinct" and from_part[0]!=select_part[0][0:len(from_part[0])]):         # table_name.colname
            for i in select_part:
                if(i!="distinct"):
                    indexes.append(answer_names.index(str(from_part[0])+"."+i))

        elif(select_part[0]=="distinct" and from_part[0]!=select_part[1][0:len(from_part[0])]):         # table_name.colname
            for i in select_part:
                if(i!="distinct"):
                    indexes.append(answer_names.index(str(from_part[0])+"."+i))
        else:
            for i in select_part:
                if(i!="distinct"):                                       # only colname
                    indexes.append(answer_names.index(i))

    return_answer=[]

    #RETURNING
    for i in final_answer:
        temp =[]
        for j in range(0,len(i)):
            if j in indexes:
                temp.append(i[j])

        return_answer.append(temp)

    return return_answer

################### END OF PROJECTIONS ####################

################### HANDLING DISTINCT #####################

def distinct_handler(answer_names,return_answer):
    answer=[]
    for i in return_answer:
        if i not in answer:
            answer.append(i)
    return answer

##################### END OF DISTINCT ######################
