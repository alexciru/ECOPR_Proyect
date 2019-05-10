""" ESTE ARCHIVO SERA MAS TARDE EL MAIN ES PARA TESTEAR EL ALGORITMO
"""

from finiteMachine import *
from bitStateHashing import *

def algorithm(*finite_machines):
    # ---------------------------------- Load FSM -----------------------
    fsm1 = FiniteMachine('A')
    fsm2 = FiniteMachine('B')
    state0 = State(0)
    state1 = State(1)
    state0.add_transition(Transition(state0, state1, '+', 'a'))
    state0.add_transition(Transition(state0, state1, '-', 'a'))
    state1.add_transition(Transition(state1, state0, '+', 'b'))
    st0 = State(0)
    st1 = State(1)
    st0.add_transition(Transition(st0, st1, '+', 'a'))
    st0.add_transition(Transition(st0, st1, '-', 'a'))
    st1.add_transition(Transition(st1, st0, '-', 'b'))
    fsm1.add_state(state0)
    fsm1.add_state(state1)
    fsm2.add_state(st0)
    fsm2.add_state(st1)
    print(fsm1)
    print(fsm2)

    bit_state_hashing = BitState("hashingtable.txt")
    bit_state_hashing.open_file()

    # -------------------- start with initial state ------------------------
    initial_state = create_initial_global_state(2)
    
    # ----------- create the stack and add the initial state ---------------
    stack = []
    stack.append(initial_state)
 
    
    

    # ---------------------- Start loop -----------------------
    while stack:
        # extract from stack the global state
        global_state = stack.pop(0) 
        print("visiting: " + str(global_state))
        # check if its already visited
        position = bit_state_hashing.hashing_function(global_state)
        print("Position: %d" % position)
        if bit_state_hashing.is_node_visited(position):
            print("\t Already visited")
            continue


        # mark as visited
        bit_state_hashing.is_node_visited(position)

        # check if have deadlock
        # TODO call function to check if have deadlock
        # if( global_state.check_deadlock() ): deadlock_counter += 1


        # figure it out the posibles transitions
            # check diagonal to see states of the FSM
        state_fsm1 = global_state[0][0]
        state_fsm2 = global_state[1][1]

            # check transitions of the state and add them to the stack 
        
        stack.append(fsm1.get_transition(state_fsm1))
        stack.append(fsm1.get_transition(state_fsm2))

        break

    print("We close the file")
    # Print results: how many deadlock does it found
    bit_state_hashing.close_file()
    return



def create_initial_global_state(n_machines):
    matrix = [[0] * n_machines] * n_machines

    for i in range(n_machines):
        for j in range(n_machines):
            if i == j:
                matrix[i][j] = '0'
            else:
                matrix[i][j] = '-'

    return matrix



def create_next_global_state(global_state, Transition):
    
    return