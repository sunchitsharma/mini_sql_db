def metadata_reader():

    # OPENING METADATA FILES
    file_desc = open ('metadata.txt','r')

    next_is_name = False # FLAG
    name = None # CURRENT FILE NAME
    answer = {} # THE RESULT {table_name : [a,b,c] }


    for row in file_desc:

        row = row.strip()

        # IF NEXT THING TO READ IS TABLE NAME
        if next_is_name == True:
            name = str(row)
            answer[name]=[]
            next_is_name = False

        # START OF A NEW TABLE
        if str(row) == '<begin_table>':
            next_is_name = True

        # ADDING COLUMS TO TABLES
        if str(row) != '<begin_table>' and str(row) != '<end_table>' and str(row) != name:
            answer[name].append(str(row))

    return answer



################# TEST CODE ###################

# metadata_reader();

###############################################
