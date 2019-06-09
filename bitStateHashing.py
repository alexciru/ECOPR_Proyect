# File: bitStateHashing.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# In this class we will be storing the information about if a state has been already visited. We will
# store this information in a File and we will decide in which position belongs to a particular state
# using a hashing function.
# 
# We will using a 16bit for the hashing function, and we will be using 2*16 = 65.535 position

# from bitstring import BitArray

class BitState:
    """
    In this class we will be storing the information about if a state has been already visited. We will
    store this information in a File and we will decide in which position belongs to a particular state
    using a hashing function.

    We will using a 16bit for the hashing function, and we will be using 2*16 = 65.535 position
    """
    
    def __init__(self, filename):
        self.f = None
        self.filename = filename
        return

    def open_file(self):
        self.f = open(self.filename, 'w+')
        self.f.write('0' * 2**16)
        # TODO cambiar tamaño por 2**16
        return

    def close_file(self):
        self.f.close()
        return

    def visit(self, position):
        """
        Go to the bit in the position pass as argument an mark it as visited with 1
        """
        self.f.seek(position)
        self.f.write('1')
        return

    def is_visited(self, position):
        """
        Check if the bit in the position is 1 (visited) or 0 (not visited)
        """
        self.f.seek(position)
        return True if self.f.read(1) == '1' else False
        

    
    

    # This is the hashing function. It will return a integer of 16bits indicating a position 
    # in the file. In order to calculate this integer it will use all the bits of the global state
    # matrix 
    def hashing_function(self, global_state):
        value = hash(str(global_state))
        value = value & 0b1111111111111111
        return value
        

    # This our version of the hashing function. We know is not very well design but it will work for the proyect
    # This version is more or less based on the one at a time jenkings function, but we cahnce some values in 
    # the number of shifting bits
    def jenkings_hashing(global_state):  
        key = str(global_state)
        lenght = len(key)
        i = 0
        mask = 0b1111111111111111
        hash_value = 0 

        while i != lenght:
            hash_value += ord(key[i]) # hash += key[i++];
        
            i += 1
            hash_value += (hash_value << 5)  # hash += hash << 10;
            hash_value = hash_value & mask
            hash_value ^= (hash_value >> 3)  # hash ^= hash >> 6;
            hash_value = hash_value & mask

        hash_value += (hash_value << 4)      # hash += hash << 3;
        hash_value = hash_value & mask
        hash_value ^= (hash_value >> 3)      # hash ^= hash >> 11
        hash_value = hash_value & mask
        hash_value = (hash_value << 1)       # hash += hash << 15;
        hash_value = hash_value & mask

        return hash_value
