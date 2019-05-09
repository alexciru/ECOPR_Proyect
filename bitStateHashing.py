# File: bitStateHashing.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# In this class we will be storing the information about if a state has been already visited. We will
# store this information in a File and we will decide in which position belongs to a particular state
# using a hashing function.
# 
# We will using a 16bit for the hashing function, and we will be using 2*16 = 65.535 position


class BitState:
    
    def __init__(self, filename):
        self.f = None
        self.filename = filename
        return

    def open_file(self):
        self.f = open(self.filename, 'w+')
        self.f.write('0' * 32)
        # TODO cambiar tamaño por 2**16
        return

    def close_file(self):
        self.f.close()
        return

    def visit_node(self, position):
        self.f.seek(position)
        self.f.write('1')
        return

    def is_node_visited(self, position):
        self.f.seek(position)
        return True if self.f.read(1) == '1' else False
        

    
    

    # This is the hashing function. It will return a integer of 16bits indicating a position 
    # in the file. In order to calculate this integer it will use all the bits of the global state
    # matrix
    #TODO change hashing function: jenkings hashing (use str function) 
    #TODO change mask lenght
    def hashing_function(self, state):
        value = hash(str(state.global_state))
        value = value & 0b11111
        return value
        
