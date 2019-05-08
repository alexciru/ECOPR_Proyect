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

class finiteMachine:

    def __init__(self, id):
        self.id = id    
        self.states = []      # Creates list of states, initialy empty
    
        return

    def add_state(self, state):
        self.states.append(state)
        return

    


    

class state:
    
    """
    This should be the class that store the information about a state of the finite machines
    variables:

    - identifier:  (A number)
    - transitions: (an array of transitions)
    """
    def __init__(self, state_id, finite_id):
        self.id = state_id
        self.transitions = []
        self.counter = 0  # how many states we already visited
        return

    def add_transition(self, transition):
        self.transitions.append(transition)
        return

    def next_transition(self):
        transition = self.transitions[self.counter]
        self.counter += 1
        return transition


class transition:
    """
    This class will storage information about transatiosns, will be store information about
    the conexion to another state , reciving or sending a signal , and the signal recieve.

    Variables:
        -  to state          (the identifier of the state)
        -  recieving/sending (+ / -)
        -  signal            (a character)
        
    """

    def __init__(self, next_state, acction, signal):
        # self.machine_id 
        self.state = next_state
        self.acction = acction
        self.signal = signal
        
        return

    