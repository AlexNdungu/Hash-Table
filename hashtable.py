# Create a list that will store all the key value pairs
# Give it a constant length 

LIST_MAX_SIZE = 4096 # Can vary

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
        pass

    #Update fuction
    def update(self, key, value):
        pass

    #List all items
    def listAll(self):
        pass


# Lets test the     