<<<<<<< HEAD
# File: main.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# TODO add comments
#

from bitStateHashing import *
from finiteMachine import *
from algorithm import *
from machineReader import *


def main():
    # Read information from the file
    #r = MachineReader()
    #r.readFile("data.txt")
    # Obtain a list of machines
    
    # start executing the algoritm
    
    deadlocks = algorithm()
    # show how many deadlocks 
 
       
    return



if __name__ == "__main__":
=======
# File: main.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# TODO add comments
#

from bitStateHashing import *
from finiteMachine import *
from algorithm import *
from machineReader import *


def main():
    # Read information from the file
    r = MachineReader()
    r.readFile("data.txt")
    # Obtain a list of machines

    # start executing the algoritm
    # deadlocks = algorithm()
    # show how many deadlocks 
       
    return
        


if __name__ == "__main__":
>>>>>>> a3e6579707e39a0e6a290609f31c14323e432d02
    main()