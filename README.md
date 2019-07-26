w# Automatic program verifier (partial exploration, with compression)

```
Add k-means Gif
```

###### This project was done in the course of Data Mining in the University Politechnika Warszawa.
![Alt text](http://www.mini.pw.edu.pl/~gagolews/mini_studia_II_stopnia_matematyka/logopw.png)
___


### Main task
The objective is to create a program to conveniently investigate the unfolding behavior of a protocol and discovers if it presents some faults. In order to explore the full protocol, we build a reachability state space checking each global state and see if present some faults such as deadlocks.

In order not to run out of memory we will implement a compression mechanism to reduce the amount of memory needed to run the program. We will use a bistate hashing, which will convert a global state into a numerical number which points to a bit in a computer memory, this bit will indicate if the node has been visited.


### input
The protocol will be represented as a set finite state machines, each one with its own number of states, transition, The FSM will be read from a simple file in a txt format, using simple software such as notepad++.
```
M0:S0,S1
   t:S0+aS1
   t:S1+bS0
   t:S0-aS1
```
Where M is the machine folowing by the states and the transitions between the states with the action needed. (+) for sending and (-) for receiving and a letter indicated the signal
### Hashing function

The hashing function will oversee converting the global state into a numerical value. This numerical value will be 16bits unsigned integer in order to point a position in the file. We took inspiration from “one_at_a_time” Jenking’s hashing function and we tried to create our own version modifying the number of positions which the bits shift.

### Algorithm
Once we store the FSM we can start with the verification of the program. We start in the initial state with all the channels empty and start checking all the following reachable global states in order to find any possible faults such as deadlocks.

We use depth-first algorithm in order to go through the reachability graph. Every state we visit we check with the bit-state-hashing function if the state has been already visited. If it’s a new state, we check for the if the Global State have a deadlock.

After checking if has deadlock we introduce the possible child in the stack and continue the execution. We limited the stack in order to avoid a problem with unboundedness and an infinite execution.

Eventually the execution will finish once the stack is empty. Some states will be ‘hidden’ due to the collision with the hashing function.

### Experiments

1. Test 1

    ![Alt text](https://media.giphy.com/media/l41lUJ1YoZB1lHVPG/giphy.gif)


2. Test 2

    ![Alt text](https://media.giphy.com/media/bAlYQOugzX9sY/giphy.gif)


3. Test 3

    Because in the previous test we could not find any deadlocks we force a new test forcing the deadlocks. We created two different machines each one with one state and no transitions.

    ![Alt text](https://media.giphy.com/media/5Zesu5VPNGJlm/giphy.gif)

    After the execution we could see that the deadlock was detected
