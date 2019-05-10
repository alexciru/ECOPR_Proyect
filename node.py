
from finiteMachine import Transition

class Node:

    def __init__(self, global_state, transaction):
        self.global_state = global_state
        self.transaction_list = transaction
        return

    def get_next_global_state(self):
        if not self.transaction: #if not transaction in the list, we already check all posible kids
            return None

        transaction = self.transaction_list.pop(0)
        length = len(self.global_state)

        new_global_state = [[0] * length] * length
        #check if is - if its a posible next state
        
        # create new global state (change state of the diagonal)
        # add or remove signal from channel

        return


    # TODO fix the function:
    def is_transition_posible(self):
        transition = self.transition[0]
        if transition.action == '+':
            # TODO check if signal bufferis full - put buffer constraids
            return True
        elif transition.action == '-':
            #check if signal is in buffer
            channel = self.global_state[transition.actual_state][transition.next_state]
            # TODO check if first letter is the signal
                #if yes: extract it and return true
                # if not: return false 
            return True
        else:
            # TODO maybe check for 'e' actions
            return True
       