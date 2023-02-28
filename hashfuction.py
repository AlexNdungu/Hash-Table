# Create a hash fuction to convert string to number to be used as index

def HashFunction(data_list, a_string):

    result = 0

    for a_char in a_string:

        a_number = ord(a_char)

        result += a_number

    #Now find the remender of the result from the length of the list
    list_index = result % len(data_list)    

    return list_index