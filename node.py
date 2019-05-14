

from finiteMachine import *
from copy import copy, deepcopy

class Node:

    def __init__(self, global_state, transaction):
        self.global_state = global_state
        self.transaction_list = transaction
        return


    # This function will return the a new global state base on the next transaction that have 
    # in the list of transitions


    def get_next_node(self, fsm):
        global_state = self.get_next_global_state()
        transaction_list = self.get_transitions(global_state, fsm)
        
        return Node(global_state, transaction_list)



    def get_next_global_state(self):
        
        
        while True: # Obtain a valid transition
            if not self.transaction_list: return None
            transaction = self.transaction_list.pop(0)

            if (self.is_transition_posible(transaction)):
                break
            
        

        print("Creating new node with t = " + str(transaction))

        length = len(self.global_state)
        
        # change the channel of the new state depending of the acction
        id_fsm = transaction.id_fsm
        other_fsm = 0 if id_fsm == 1 else 1 # TODO change this for more flexibility

        channel = self.global_state[id_fsm][other_fsm]  
        print("channel = " + channel)

        
        new_global_state = deepcopy(self.global_state)

        if(transaction.acction == '+'):
            new_chanel = transaction.signal + channel

        elif(transaction.acction == '-'):
            new_chanel = channel[1:]

        else:
            new_chanel = channel
            
        new_global_state[id_fsm][other_fsm] = new_chanel
        
        # change the diagonal
        id_fsm = transaction.id_fsm
        new_global_state[id_fsm][id_fsm] = transaction.next_state.id

        return new_global_state



    # This function will return the transitions given a matrix of state
    def get_transitions(self, global_state, fsm):
        transitions_list = []
        for i in range(len(fsm)):
            state = global_state[i][i]

            #print("[%d][%d] -- state: %c "%( i, i, state))
            transitions = fsm[i].get_transition(state)
            for t in transitions:
                transitions_list.append(t)
        
        return transitions_list


    
    def is_transition_posible(self, transition):
        transition = transition
        # We obtain the channel
        channel = self.global_state[transition.actual_state.id][transition.next_state.id]
        if transition.acction == '+':
            return True if (len(channel) <= 3) else False
            # TODO change maximum buffer size
        elif transition.action == '-':
            #check if signal is in the last input in buffer
            return True if(channel[0] == transition.signal) else True
            
        else:
            # must be a 'e' action
            return True
       


    def __str__(self):
        string = "Node" + "\t - "+ str(self.global_state)
        
        #for transition in self.transaction_list:
        #   string += "\n\t - " + str(transition) + "\n"

        return string