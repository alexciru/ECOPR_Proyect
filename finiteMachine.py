# File: finiteMachine.py
# Authors:
# Description:
# Should we store one FSM in each instance of this class or should we store the hole protocol ( various finite machines)
#   maybe the second one.
#   maybe we should create another two classees: state and transition
#   Variables:
#       - identifiair
#       - states
#

class FiniteMachine:
    """
    This class should store the information about the finite state machine
    attributes that will need:
        - identifiar of the state finite
        - list of states of the machine
        - indicator with indicates the actual state of the machine

    state_id should be a sequential number starting ftom 0 as a initial state
    initial state should be have identifier = 0
    """
    def __init__(self, identifier):
        self.id = identifier
        self.states = []      # Creates list of states, initialy empty
        self.actual_state = 0 # assig the initial state
        return

    def add_state(self, state):
        self.states.append(state)
        return

    
    def add_transition(self, state_id, next_state, acction, signal):
        transition = Transition(next_state, acction, signal)
        self.states[state_id].add_transition(transition)
        return


    def get_transition(self, state_id):
        return self.states[state_id].get_transactions()
    

    def __str__(self):
        string = "Finite Machine: %c \n" % self.id
        for i in range(len(self.states)):
            string += str(self.states[i])
            
        return string
            


    

class State:
    
    """
    This should be the class that store the information about a state of the finite machines
    variables:

    - identifier of the state machine
    - identifier:  (A number)
    - transitions: (an array of transitions)
    - counter: keep track how many transitions we already visited
    
    """
    def __init__(self, state_id):
        self.id = state_id
        self.transitions = []
        self.counter = 0  # how many states we already visited
        return

    def add_transition(self, transition):
        self.transitions.append(transition)
        return

    def get_transitions(self):
        return self.transitions

    def next_transition(self):
        transition = self.transitions[self.counter]
        self.counter += 1
        return transition

    def __str__(self):
        string = "S%d: %d transacctions:\n" % (self.id, len(self.transitions))
        for i in range(len(self.transitions)):
            string += "\t - " + str(self.transitions[i]) + "\n"

        return string
    


class Transition:
    """
    This class will storage information about transatiosns, will be store information about
    the conexion to another state , reciving or sending a signal , and the signal recieve.

    Variables:
        -  identifier of the state machine
        -  to state          (the identifier of the state)
        -  recieving/sending (+ / -)
        -  signal            (a character)
        
    """

    def __init__(self, id_fsm, from_state, to_state, acction, signal):
        self.id_fsm = id_fsm
        self.actual_state = from_state 
        self.next_state = to_state
        self.acction = acction
        self.signal = signal
        
        return

    def __str__(self):
        string = "Transition to S%d: %c %c" % (self.next_state.id , self.acction, self.signal)
        return string

    

    