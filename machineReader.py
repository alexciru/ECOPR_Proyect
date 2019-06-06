from io import *
from finiteMachine import *

class MachineReader:

    def __init__(self):
        self.document = None
        self.machines = []
        return

    def readFile(self, file):
        self.document = open(file, "r")
        info = self.document.readlines()
        fsm_id = 0
        state_id = 0
        for i in info:
           #print(i)
            for j in i:
                #print(j)
                if j > '0' and j < '9':
                    fsm_id+=1
                    fsm = FiniteMachine(fsm_id)
                    #print("se ha creado una maquina ", fsm_id)
                elif j == "A" or j == "B" or j == "C":
                    state_id+=1
                    state = State(state_id)
                    fsm.add_state(state)
                    #print("se ha creado un estado ", j)
                elif j == "+" or j == "-":
                    num = i.index(j)
                    #print(num)
                    transition = Transition(fsm_id, i[num-1], i[num+2], j, i[num+1])
                    state.add_transition(transition)
                    fsm.add_transition(fsm_id, state_id, i[num+2], j, i[num+1])
                    #print("se ha creado una transicion", fsm_id, i[num-1], i[num+2], j, i[num+1])
            self.machines.append(fsm)
            #print("una maquina añadida a la lista")
            fsm_id+=1
            state_id+=1
        return self.machines
