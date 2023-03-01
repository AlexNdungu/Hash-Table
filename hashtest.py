# Now lets test the hashtable
from hashtable import HashTable

hashtable1 = HashTable(max_size = 1024)

#print(len(hashtable1.key_value_list))

# Now insert some values
hashtable1.insert('alex', 'alex@gmail.com')
hashtable1.insert('xela', 'xela@gmail.com')

# Now we find an item
hashtable1.find('xela')

# Now lets update
hashtable1.update('xela','xelanew@gmail.com')
hashtable1.find('alex')

# List all the items added
hashtable1.listAll()