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