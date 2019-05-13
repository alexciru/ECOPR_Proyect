

from finiteMachine import *
from copy import copy, deepcopy

class Node:

    def __init__(self, global_state, transaction):
        self.global_state = global_state
        self.transaction_list = transaction
        return


    # This function will return the a new global state base on the next transaction that have 
    # in the list of transactions


    def get_next_node(self):
        global_state = get_next_global_state(self)
        transaction_list = get_transitions(global_state)
        
        return Node(global_state, transaction_list)



    def get_next_global_state(self):
        if not self.transaction: #if not transaction in the list, we already check all posible kids
            return None

        transaction = self.transaction_list.pop(0)
        length = len(self.global_state)

        
        # change the channel of the new state depending of the acction
        channel = self.global_state[transaction.actual_state][transaction.next_state]
        
        if (self.is_transition_posible()):
            new_global_state = self.global_state.deepcopy()
            if(transaction.action == '+'):
                new_chanel = transaction.signal + channel
            elif(transaction.action == '-'):
                new_chanel = channel[1:]
            else:
                new_chanel = channel
            
            new_global_state[transaction.actual_state][transition.next_state] = new_chanel
            
        return new_global_state



    # This function will return the transitions given a matrix of state
    def get_transitions(self, global_state, **fsm):
        transitions_list = []
        for i in range(fsm):
            state = global_state[i][i]
            transitions_list.append(fsm[i].get_transition(state))
        
        return transaction_list


    
    def is_transition_posible(self):
        transition = self.transition[0]
        # We obtain the channel
        channel = self.global_state[transition.actual_state][transition.next_state]
        if transition.action == '+':
            if (len(channel <= 10)): return True
            else: return False
            # TODO change maximum buffer size
        elif transition.action == '-':
            #check if signal is in the las input in buffer
            print("Chanel = " + channel)
            if(channel[0] == signal): return True
            else: return False
            
        else:
            # must be a 'e' action
            return True
       