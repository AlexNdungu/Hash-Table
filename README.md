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

### Lets Test The fuction

```
LIST_MAX_SIZE = 4096 # Can be of any length

key_value_list = [None] * LIST_MAX_SIZE

print(HashFunction(key_value_list, 'test'))

# The result is 448

```

### Lets Create a class that will handle the HashTable Crud Operations

```
# Create a list that will store all the key value pairs
# Give it a constant length 

LIST_MAX_SIZE = None # Can vary

#key_value_list = [None] * LIST_MAX_SIZE

# Lets create a hash class

from hashfuction import HashFunction

#lets test the hash fuction

class HashTable:

    def __init__(self, max_size = LIST_MAX_SIZE):
        
        #Now we create the table
        self.key_value_list = [None] * max_size

    #Insert fuction
    def insert(self, key, value):
        
        #Lets get the index generated from the key
        new_index = HashFunction(self.key_value_list, key)

        #Now we insert the value to the index

        self.key_value_list[new_index] = key,value

        return print('Item Added To List')

    #Find fuction
    def find(self, key):
        
        # first find the index
        find_index = HashFunction(self.key_value_list, key)

        kv = self.key_value_list[find_index]

        if kv is None:
            return None
        else:
            key, value = kv
            return print(value)

    #Update fuction
    def update(self, key, value):
        
        # first find the index
        update_index = HashFunction(self.key_value_list, key)

        self.key_value_list[update_index] = key, value


    #List all items
    def listAll(self):
        
        return print([key_value[0] for key_value in self.key_value_list if key_value is not None])


```

### Test the HashTable Class

```

# Now lets test the hashtable
from hashtable import HashTable

hashtable1 = HashTable(max_size = 1024)

#print(len(hashtable1.key_value_list))

# Now insert some values
hashtable1.insert('alex', 'alex@gmail.com')
hashtable1.insert('meta', 'meta@gmail.com')

# Now we find an item
hashtable1.find('meta')

# Now lets update
hashtable1.update('meta','metanew@gmail.com')
hashtable1.find('meta')

# List all the items added
hashtable1.listAll()

```

### Handling Collisions

```

# Now lets handle collisions

from hashfuction import HashFunction

def avoid_collision(data_list, key):

    the_index = HashFunction(data_list, key)

    while True:

        key_value = data_list[the_index]

        #If the index position is empty, then return the index
        if key_value is None:
            return the_index
        
        # If the stored key matches the given key, return the index
        search_key, search_value = key_value
        if search_key == key:
            return the_index
        
        # Move to the next index
        the_index += 1

        #Go back to the start when array ends
        if the_index == len(data_list):
            the_index = 0
            
```