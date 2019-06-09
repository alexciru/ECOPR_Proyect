# File: main.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# This Main function is in charge to call to different function to properly execute the project.
# First call to the MachineReader class to create the FSM. And them call the algorithm in order to 
# check how many deadlocks can found.
# After the execution of the algorithm will print how many deadlocks does it found and the execution time.

from bitStateHashing import *
from finiteMachine import *
from algorithm import *
from machineReader import *
import time


def main():
    # Read information from the file
    r = MachineReader()
    r.readFile("data2.txt")

    for i in r.machines:
        print(i)

    #for machine in r.machines : print(machine)
    
    # start executing the algoritm
    start_time = time.time()
    deadlocks = algorithm(r.machines)
    final_time = time.time()
    execution_time = final_time - start_time
    print("We found %d deadlocks."% deadlocks)
    print("Execution time of the algorith is: %f " % execution_time)
    return



if __name__ == "__main__":
    main()