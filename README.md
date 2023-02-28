# Building A Hash Table From Scratch

**HASH TABLE** &rarr; a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value.

**HASH FUCTION** &rarr; Used to convert strings and non-numeric data types into numbers, which can then be used as list indices.

![Hash Table](https://svbtleusercontent.com/dvp2mqhvzcqyqa.jpg)

### Hash Fuction Code

```

# Create a hash fuction to convert string to number to be used as index

def HashFunction(data_list, a_string):

    result = 0

    for a_char in a_string:

        a_number = ord(a_char)

        result += a_number

    #Now find the remender of the result from the length of the list
    list_index = result % len(data_list)    

    return list_index

```
