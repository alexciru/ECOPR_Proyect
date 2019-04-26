# File: finiteMachine.py
# Authors:
# Description:
# This class will be in charge of storing the information about the protocol in form of a FSM.
#

class finiteMachine:

    id = 1
    """
    Should we store one FSM in each instance of this class or should we store the hole protocol ( various finite machines)
    maybe the second one.


    maybe we should create another two classees: node and transition
    Variables:
        - identifiair
        - states
    """

    def __init__(self):
        self.id = id
        id += 1

    
        return

    

class state:
    
    """
    This should be the class that store the information about a state of the finite machines
    variables:

    - identifier:  (A number)
    - transitions: (an array of transitions)
    """
    def __init__(self, id):
        self.id = id
        self.transitions = []
        return

    def add_transition(self, transition):
        self.transitions.append(transition)
        return


class transition:
    """
    This class will storage information about transatiosns, will be store information about
    the conexion to another state , reciving or sending a signal , and the signal recieve.

    Variables:
        -  to state          (the identifier of the state)
        -  recieving/sending (+ / -)
        -  signal            (a character)
        
    """

    def __init__(self, state, acction, signal):
        self.state = state
        self.acction = acction
        self.signal = signal
        return