# Create a list that will store all the key value pairs
# Give it a constant length 

LIST_MAX_SIZE = None # Can vary

#key_value_list = [None] * LIST_MAX_SIZE

# Lets create a hash class

from hashcollisions import avoid_collision

#lets test the hash fuction

class HashTable:

    def __init__(self, max_size = LIST_MAX_SIZE):
        
        #Now we create the table
        self.key_value_list = [None] * max_size

    #Insert fuction
    def insert(self, key, value):
        
        #Lets get the index generated from the key
        new_index = avoid_collision(self.key_value_list, key)

        #Now we insert the value to the index

        self.key_value_list[new_index] = key,value

        return print('Item Added To List')

    #Find fuction
    def find(self, key):
        
        # first find the index
        find_index = avoid_collision(self.key_value_list, key)

        kv = self.key_value_list[find_index]

        if kv is None:
            return None
        else:
            key, value = kv
            return print(value)

    #Update fuction
    def update(self, key, value):
        
        # first find the index
        update_index = avoid_collision(self.key_value_list, key)

        self.key_value_list[update_index] = key, value


    #List all items
    def listAll(self):
        
        return print([key_value[0] for key_value in self.key_value_list if key_value is not None])

