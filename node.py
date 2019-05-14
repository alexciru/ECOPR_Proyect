

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
        if not self.transaction_list: #if not transaction in the list, we already check all posible kids
            return None

        transaction = self.transaction_list.pop(0)
        
        print("Creating new Node: Transition == " + str(transaction))
        length = len(self.global_state)

        
        # change the channel of the new state depending of the acction

        from_id = transaction.actual_state.id
        to_id = transaction.next_state.id

        channel = self.global_state[from_id][to_id]
        
        if (self.is_transition_posible( transaction)):
            new_global_state = deepcopy(self.global_state)
            if(transaction.acction == '+'):
                new_chanel = transaction.signal + channel
            elif(transaction.acction == '-'):
                new_chanel = channel[1:]
            else:
                new_chanel = channel
            
            new_global_state[transaction.actual_state.id][transaction.next_state.id] = new_chanel
            
        return new_global_state



    # This function will return the transitions given a matrix of state
    def get_transitions(self, global_state, fsm):
        transitions_list = []
        for i in range(len(fsm)):
            state = global_state[i][i]
            
            #transitions_list.append(fsm[i].get_transition(state))
            transitions = fsm[i].get_transition(state)
            for t in transitions: 
                transitions_list.append(t)
        
        return transitions_list


    
    def is_transition_posible(self, transition):
        transition = transition
        # We obtain the channel
        channel = self.global_state[transition.actual_state.id][transition.next_state.id]
        if transition.acction == '+':
            if (len(channel) <= 10): return True
            else: return False
            # TODO change maximum buffer size
        elif transition.action == '-':
            #check if signal is in the las input in buffer
            if(channel[0] == transition.signal): return True
            else: return False
            
        else:
            # must be a 'e' action
            return True
       


    def __str__(self):
        string = "Node" + "\t - "+ str(self.global_state) + "\n"
        for transition in self.transaction_list:
            string += "\t - " + str(transition) + "\n"

        return string