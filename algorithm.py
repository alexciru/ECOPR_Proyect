from finiteMachine import *



def algorithm(*finite_machines):
    # read finite machines
    fsm1 = FiniteMachine('A')
    fsm2 = FiniteMachine('B')

    state0 = State(0)
    state1 = State(1)
    state0.add_transition(Transition(state1, '+', 'a'))
    state0.add_transition(Transition(state1, '-', 'a'))
    state1.add_transition(Transition(state0, '+', 'b'))

    st0 = State(0)
    st1 = State(1)
    st0.add_transition(Transition(st1, '+', 'a'))
    st0.add_transition(Transition(st1, '-', 'a'))
    st1.add_transition(Transition(st0, '-', 'b'))
    


    fsm1.add_state(state0)
    fsm1.add_state(state1)
    fsm2.add_state(st0)
    fsm2.add_state(st1)

    print(fsm1)
    print(fsm2)


    # start with initial state
    initial_state = create_initial_global_state(2)
    
    stack = []
    stack.append(initial_state)

    #loop: (stack not empty)
    while stack:
        # figure it out the posibles transitions
        # take first option
        # check if already visited
        break

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