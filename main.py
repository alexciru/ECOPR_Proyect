# File: main.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# TODO add comments
#


def main():
    # Read information from the file
    # start executing the algoritm
    # show how many deadlocks
    print("Probar test")
    test_matrix = [['a','-','-'],
                  ['-','b','-'],
                  ['-','-','c']]

    value = hashing_function(test_matrix)
    print(value)
    return


#TODO change hashing function: jenkings hashing 
def hashing_function(global_state):

    value = global_state.__hash__
    value & 0b1111111111111111
   
    return value
        

if __name__ == "__main__":
    main()