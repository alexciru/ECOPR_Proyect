# File: main.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# TODO add comments
#

from bitStateHashing import *
from finiteMachine import *

test_matrix = [['a','-','-'],
               ['-','b','-'],
               ['-','-','c']]

def main():
    # Read information from the file
    # start executing the algoritm
    # show how many deadlocks  

       
    return










#TODO change hashing function: jenkings hashing (use str function) 
def hashing_function(state):
    value = hash(str(state.global_state))
    value = value & 0b1111111111111111
    #value = bin(value)
    return value
        

def is_deadlock(state):
    # TODO comprobar si el estado pasado por argumento tiene o no deadlock
    return


if __name__ == "__main__":
    main()