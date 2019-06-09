# File: algorithm.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# In this file is the execution of the algorithm of the validation. We create a initial global state and using depth-first algortith
# to travel across the reachability graph and checking if contain any deadlock.
#
# CONSRAINTS:
#      - The stack size is limited to 100 elements

from finiteMachine import *
from bitStateHashing import *
from node import *

def algorithm(machines):

    # create file for the hashing table
    bit_state_hashing = BitState("hashingtable.txt")
    bit_state_hashing.open_file()
    
    print("\n\n -------------Algorith start -------------")

    initial_node = create_initial_node(machines)
    # ----------- create the stack and add the initial state ---------------
    initial_node.visit_node
    stack = []
    stack.append(initial_node)
 
    initial_node.visit_node(bit_state_hashing)
    deadlock_counter = 0
    states_visited = 1 #count the initial state

    # start of the loop
    while stack:
        # We check the last element of the stack without removing it
        actual_node = stack[-1]
 
        child_node = actual_node.get_next_node(machines)
        if (child_node == None):    #if no node is created, it dont have more transition left
            stack.pop()
        else: 
            if(not child_node.is_node_visited(bit_state_hashing)):
                child_node.visit_node(bit_state_hashing) #mark as visited and add to stack
                states_visited += 1
                if( child_node.check_deadlock() ): deadlock_counter += 1

                if(len(stack) < 100):    # We limited the size of the stack to 100
                    stack.append(child_node)



    #close the file with the hashing table
    print("Algorithm finished with %d states visited" % states_visited)
    bit_state_hashing.close_file()
    return deadlock_counter





def create_initial_node(fsm):
    """
    Return a Node instance with the information of the inital node necesary for the algorithm.
    It will be the initial global state and the initial transactions of the fsm.
    """
    global_state = create_initial_global_state(len(fsm))    
  
    # check transitions of the state and add them to the stack 
    transitions_list = []
    for i in range(len(fsm)):
        state = global_state[i][i]
        
        machine = fsm[i]
        transitions = machine.get_transition(state)
        for t in transitions: 
            transitions_list.append(t)
     
    node = Node(global_state, transitions_list)
    return node






def create_initial_global_state(n_machines):
    """
    Will return a matrix representing the inital global state:
    All channels empty and in the state 0 in every machine.
    """
    matrix = [['' for i in range(n_machines)] for j in range(n_machines)]

    for i in range(n_machines):
        matrix[i][i] = '0'

    return matrix

