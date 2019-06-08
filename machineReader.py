from io import *
from finiteMachine import *

class MachineReader:

    def __init__(self):
        self.document = None
        self.machines = []
        return

    def readFile(self, file):
        self.document = open(file, "r")
        for line in self.document:
            if line[0] == "M":
                fsm_id = line[1]
                fsm = FiniteMachine(int(fsm_id))
                self.machines.append(fsm)
                sub_list = line.split(":")
                state_list = sub_list[1].split(",")
                for token in state_list:
                    state = State(int(token[1]))
                    fsm.add_state(state)
            elif line[0] == "t":
                transition_list = line.split(":")
                for m in transition_list[1]:
                    if m == "+" or m == "-":
                        k = line.index(m)
                        index_or = int(line[k-1])
                        original_state = fsm.states[index_or]
                        index_dest = int(line[k+3])
                        destination_state = fsm.states[index_dest]
                        transition = Transition(int(fsm_id), original_state, destination_state, m, line[k+1])
                        fsm.states[int(line[k-1])].add_transition(transition)
            else:
                print("ERROR: The file provides incorrect information\n")
                return
    
        return self.machines