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