<<<<<<< HEAD
# File: algorithm.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# In this file is the execution of the algorithm of the validation. We create a initial global state and using depth-first algortith
# to travel across the reachability graph and checking if contain any deadlock.
#
from finiteMachine import *
from bitStateHashing import *
from node import *

def algorithm(*finite_machines):
    # ---------------------------------- Load FSM -----------------------
    fsm1 = FiniteMachine(0)
    fsm2 = FiniteMachine(1)
    state0 = State(0)
    state1 = State(1)
    state0.add_transition(Transition(0, state0, state1, '+', 'a'))
    state0.add_transition(Transition(0, state0, state1, '-', 'a'))
    state1.add_transition(Transition(0,state1, state0, '+', 'b'))
    st0 = State(0)
    st1 = State(1)
    st0.add_transition(Transition(1, st0, st1, '+', 'a'))
    st0.add_transition(Transition(1, st0, st1, '-', 'a'))
    st1.add_transition(Transition(1, st1, st0, '-', 'b'))
    fsm1.add_state(state0)
    fsm1.add_state(state1)
    fsm2.add_state(st0)
    fsm2.add_state(st1)
    print(fsm1)
    print(fsm2)

    machines = []
    machines.append(fsm1)
    machines.append(fsm2)

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

    # ---------------------- Start loop -----------------------
    while stack:
        # We check the last element of the stack without removing it
        actual_node = stack[-1]
        print("\n")
        print("visiting: " + str(actual_node))
 

        # check if have deadlock
        # TODO call function to check if have deadlock
        if( global_state.check_deadlock() ): deadlock_counter += 1

        
        child_node = actual_node.get_next_node(machines)
        if (child_node == None): #if no node is created, it dont have more transition left
            print("No node created")
            stack.pop()
        else: 
            if(not child_node.is_node_visited(bit_state_hashing)):
                child_node.visit_node(bit_state_hashing)
                if(len(stack) < 100):
                    stack.append(child_node)
                    print("adding to stack: " +str(actual_node)+" ----> " + str(child_node))


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

=======
# File: algorithm.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# TODO add comments
#
from finiteMachine import *
from bitStateHashing import *
from node import *

def algorithm(*finite_machines):
    # ---------------------------------- Load FSM -----------------------
    fsm1 = FiniteMachine(0)
    fsm2 = FiniteMachine(1)
    state0 = State(0)
    state1 = State(1)
    state0.add_transition(Transition(0, state0, state1, '+', 'a'))
    state0.add_transition(Transition(0, state0, state1, '-', 'a'))
    state1.add_transition(Transition(0,state1, state0, '+', 'b'))
    st0 = State(0)
    st1 = State(1)
    st0.add_transition(Transition(1, st0, st1, '+', 'a'))
    st0.add_transition(Transition(1, st0, st1, '-', 'a'))
    st1.add_transition(Transition(1, st1, st0, '-', 'b'))
    fsm1.add_state(state0)
    fsm1.add_state(state1)
    fsm2.add_state(st0)
    fsm2.add_state(st1)
    print(fsm1)
    print(fsm2)

    machines = []
    machines.append(fsm1)
    machines.append(fsm2)

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

    # ---------------------- Start loop -----------------------
    while stack:
        # We check the last element of the stack without removing it
        actual_node = stack[-1]
        print("\n")
        print("visiting: " + str(actual_node))
 

        # check if have deadlock
        # TODO call function to check if have deadlock
        # if( global_state.check_deadlock() ): deadlock_counter += 1


        
        child_node = actual_node.get_next_node(machines)
        if (child_node == None): #if no node is created, it dont have more transition left
            print("No node created")
            stack.pop()
        else: 
            if(not child_node.is_node_visited(bit_state_hashing)):
                child_node.visit_node(bit_state_hashing)
                if(len(stack) < 100):
                    stack.append(child_node)
                    print("adding to stack: " +str(actual_node)+" ----> " + str(child_node))





    # TODO Print results: how many deadlock does it found
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

>>>>>>> a3e6579707e39a0e6a290609f31c14323e432d02
