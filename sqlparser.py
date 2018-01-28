import sqlparse
import sys

def getquery(arg):
    arg = sqlparse.split(str(arg))
    for query in arg:
        select_part=[]
        from_part=[]
        where_part=[]
        q_break = sqlparse.parse(query)
        q_tokens = q_break[0].tokens

        ############ EXTRACTING SELECT PART ##############
        flag = False

        for i in q_tokens:
            if(str(i)=='select'):
                flag = True
            if(str(i)[0:5]=="where" or str(i)=="from"):
                flag = False
            if(flag == True and str(i)!='select' and str(i)!=" "):
                to_add = str(i).split(',')
                select_part.extend(to_add)

        print "SELECT : "+str(select_part)

        ############## EXTRACTING FROM PART ##############

        flag = False

        for i in q_tokens:
            if(str(i)=='from'):
                flag = True
            if(str(i)=="select" or str(i)[0:5]=="where"):
                flag = False
            if(flag == True and str(i)!='from' and str(i)!=" "):
                to_add = str(i).split(',')
                from_part.extend(to_add)

        print "FROM : "+str(from_part)

        ############## EXTRACTING WHERE PART ##############

        if(str(q_tokens[-1])[0:5]=="where"):
            where_part.append(str(q_tokens[-1])[5:])

        print "WHERE : "+str(where_part)


#################### TEST CODE ################

# getquery(sys.argv[1])

###############################################
