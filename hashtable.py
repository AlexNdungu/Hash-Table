# Create a list that will store all the key value pairs
# Give it a constant length 

LIST_MAX_SIZE = 4096

key_value_list = [None] * LIST_MAX_SIZE

# Lets create a hash class

from hashfuction import HashFunction

#lets test the hash fuction
print(HashFunction(key_value_list, 'test'))

class HashTable:

    #Insert fuction
    def insert(self, key, value):
        pass

    #Find fuction
    def find(self, key):
        pass

    #Update fuction
    def update(self, key, value):
        pass

    #List all items
    def listAll(self):
        pass