""" ESTE ARCHIVO SERA MAS TARDE EL MAIN ES PARA TESTEAR EL ALGORITMO
"""
# TODO stack is not pushiong propperly

from finiteMachine import *
from bitStateHashing import *
from node import *

def algorithm(*finite_machines):
    # ---------------------------------- Load FSM -----------------------
    fsm1 = FiniteMachine(1)
    fsm2 = FiniteMachine(2)
    state0 = State(0)
    state1 = State(1)
    state0.add_transition(Transition(1, state0, state1, '+', 'a'))
    state0.add_transition(Transition(1, state0, state1, '-', 'a'))
    state1.add_transition(Transition(1,state1, state0, '+', 'b'))
    st0 = State(0)
    st1 = State(1)
    st0.add_transition(Transition(2, st0, st1, '+', 'a'))
    st0.add_transition(Transition(2, st0, st1, '-', 'a'))
    st1.add_transition(Transition(2, st1, st0, '-', 'b'))
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
    
    

    initial_node = create_initial_node(machines)
    # ----------- create the stack and add the initial state ---------------
    
    stack = []
    stack.append(initial_node)
 
    
    """ At this point we only this variables:
            - machines:             list of fsm read from file
            - bit_state_hashing:    class to check if a node has been visited
            - stack:                list of class Nodes. Right now with the initial state
    """
    

    # ---------------------- Start loop -----------------------
    while stack:
        # We check the last element of the stack without removing it
        actual_node = stack[0]
        print("visiting: " + str(actual_node.global_state))
        

        # We check the positon of the hashi
        position = bit_state_hashing.hashing_function(actual_node.global_state)
        print("Position: %d" % position)


        #if visited jump to the next node
        if bit_state_hashing.is_node_visited(position):
            print("\t Already visited")
            stack.pop() #we remove it
            continue



        # if not, mark as visited
        bit_state_hashing.visit_node(position)


        # check if have deadlock
        # TODO call function to check if have deadlock
        # if( global_state.check_deadlock() ): deadlock_counter += 1


        # We obtain the first child and we added to the stack
        print("noddeeeee")
        print(actual_node)

        child_node = actual_node.get_next_global_state()

        if (child_node == None): stack.remove(0) #we remove it
        else: stack.append(child_node)



    print("We close the file")
    # Print results: how many deadlock does it found
    bit_state_hashing.close_file()
    return





def create_initial_node(fsm):
    global_state = create_initial_global_state(len(fsm))    
  
    # check transitions of the state and add them to the stack 
    transitions_list = []
    print("matrix2  -->" + str(global_state))
    for i in range(len(fsm)):
        state = global_state[i][i]
        
        machine = fsm[i]
        print(machine)
        transitions = machine.get_transition(state)
        for t in transitions: 
            transitions_list.append(t)
     
    node = Node(global_state, transitions_list)
    return node






def create_initial_global_state(n_machines):
    matrix = [['-' for i in range(n_machines)] for j in range(n_machines)]

    for i in range(n_machines):
        matrix[i][i] = '0'

    return matrix

