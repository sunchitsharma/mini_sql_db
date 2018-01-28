import csv

def filereader(name):

    # OPENING THE FILE
    file_desc = open (name+".csv" ,'r' )
    # READING THE CSV FILE
    csvread = csv.reader(file_desc)

    answer=[] # TABLE TO BE RETURNED

    for row_i in csvread:
        answer.append(row_i)

    return answer # ANSWER AS LIST IN A LIST : ROW-WISE


################## TEST CODE ####################

# print filereader('table1')

#################################################
