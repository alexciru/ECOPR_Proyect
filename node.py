# File: node.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# The Node class is a class used for the verifier algorithm. This class is in charge to storage all 
# all the information needed for the "nodes" of the reachability graph. Storing the gloabl stte and
# the posible transaction that havent been visited yet

from finiteMachine import *
from bitStateHashing import *
from copy import copy, deepcopy

class Node:
    """
    The Node class is the representation of a node in the transition tree. Every Node have information 
    about the current state: global_state. And also store information about the posible transictions to 
    next nodes.
    """

    def __init__(self, global_state, transaction):
        self.global_state = global_state
        self.transaction_list = transaction
        return


    # This function will return the a new global state base on the next transaction that have 
    # in the list of transitions


    def get_next_node(self, fsm):
        """
        Return a new node created by the actual state + the next transition in the list
        """

        global_state = self.get_next_global_state()
        if global_state == None: return None
        transaction_list = self.get_transitions(global_state, fsm)
        
        return Node(global_state, transaction_list)



    def get_next_global_state(self):
        """
        Create a new matrix of global state modifying the channel depending of the next transition
        """

        while True: # Obtain a valid transition
            if not self.transaction_list:
                return None

            transaction = self.transaction_list.pop(0)
            if (transaction):
                if (self.is_transition_posible(transaction)):
                    break
            
    
        #print("Creating new node with t = " + str(transaction))
        length = len(self.global_state)
        
        # change the channel of the new state depending of the action
        id_fsm = transaction.id_fsm
        other_fsm = 0 if id_fsm == 1 else 1 # TODO change this for more flexibility
        channel = self.global_state[other_fsm][id_fsm]  
        
        new_global_state = deepcopy(self.global_state)

        if(transaction.action == '+'):
            new_chanel = transaction.signal + channel

        elif(transaction.action == '-'):
            new_chanel = channel[1:]

        else:
            new_chanel = channel
            
        new_global_state[id_fsm][other_fsm] = new_chanel
        
        # change the diagonal
        id_fsm = transaction.id_fsm
        new_global_state[id_fsm][id_fsm] = transaction.next_state.id

        return new_global_state


    def get_transitions(self, global_state, fsm):
        """
        Will return transaction given the actual states of the machines
        """
        transitions_list = []
        for i in range(len(fsm)):
            state = global_state[i][i]

            #print("[%d][%d] -- state: %c "%( i, i, state))
            transitions = fsm[i].get_transition(state)
            for t in transitions:
                transitions_list.append(t)
        
        return transitions_list


    
    def is_transition_posible(self, transition):
        """
        Check if a transaction is possible depending of the actual global state. It check
        the maximum buffer channel size and if its recieving signal if its in first position 
        of the channel
        """
        if not transition: return False
        
        id_other_fsm = 1 if transition.id_fsm == 0 else 0
        channel = self.global_state[id_other_fsm][transition.id_fsm]
       
        if transition.action == '+':
            return True if (len(channel) <= 10) else False
        elif transition.action == '-':
            #check if signal is in the last input in buffer
            if not channel: return False
            return True if(channel[0] == transition.signal) else True
            
        else:
            # must be a 'e' action
            return True
       


    def is_node_visited(self, bitstate_hashing):
        """
        Call the bisStateHashing class to check if a state has already been visited
        """
        #position = bitstate_hashing.hashing_function(self.global_state)
        position = bitstate_hashing.jenkings_hashing(self.global_state)
        
        if bitstate_hashing.is_visited(position):
            #print("\t Node Already visited")
            return True
        
        return False

    def visit_node(self, bitstate_hashing):
        """
        Call the bistateHashing class to mark a global state as visited
        """
        #position = bitstate_hashing.hashing_function(self.global_state)
        position = bitstate_hashing.jenkings_hashing(self.global_state)
        bitstate_hashing.visit(position)
        return

    def check_deadlock(self):
        """
        Check if the actual global state contain any deadlock. Deadlock its the global state which has no posible
        posible transactions to the next state. This functions check if there is at least one posible transaction
        """
        for transaction in self.transaction_list:
            if self.is_transition_posible(transaction):
                return False

        print("Deadlock Found")
        print(self.global_state)
        return True

    def __str__(self):
        string = "\n+ Node" + "\t - "+ str(self.global_state)
        # for transition in self.transaction_list:
        #    string += "\n\t - " + str(transition)

        return string

    def __repr__(self):
        return str(self)