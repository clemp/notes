import numpy as np
import math
import matplotlib.pyplot as plt

# Choose function
def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def update(p):
    # Game of Life rules as probabilities
    '''
    Each quiescent (dead, off) cell will turn into a living (on) cell if and only if it is surrounded by exactly three living cells; 
    A living cell will remain alive if and only if it is surrounded by two or three other living cells; otherwise it will die

    p: density of alive (on) cells
    (1-p): density of dead (off) cells

    A: probability of an alive cell to stay alive
    B: probability of a dead cell to become alive

    nextp: weighted average of alive cells
    '''
    ## Probabilities of either being dead or alive in the current state.
    # probability of the event for cells to go from dead to alive (at a grid level).
    B = nCr(8, 3) * (p**3) * (1 - p)**5 
    
    # probability of the event for cells to go from alive cell to staying alive (at a grid level).
    A = nCr(8, 2) * (p**2) * (1 - p)**6 + B 

    ## Given the current state, probability of the next state.
    nextp = p * A + (1 - p) * B
    return nextp

if __name__ == "__main__":
    domain = np.linspace(0, 1, 100)
    plt.plot(domain, update(domain))
    plt.plot(domain, domain)
    plt.show()