# Constraint Satisfaction

Implemented the backtracking algorithm to solve two constraint satisfaction problems: **Map Coloring** and **Circuit Board**. 

Backtracking has a reduced time complexity of **O(d^n)** compared to **O(n!d^n)** for a standard search, where n is number of variables and d is size of domain. This is because the backtracking algorithm only explores the d^n possible assignments, while a standard search explores all possible permutations of those d^n assignments.

* **Map Coloring** – Each state in Australia is assigned a color such that no two neighboring states share the same color.

* **Circuit Board** – Components of varying width and height are fit onto the circuit board such that no two pieces collide.

### Backtracking Algorithm

The Backtracking Algorithm recursively assigns a value to a variable and checks if the constraints are satisfied. If not, the algorithm will "backtrack" and try other assignments. Two key distinctions for backtracking algorithm:

1. One variable at a time – We only consider assignments to a single variable at each step. By arbitrarily choosing a fixed order to assign variables, we reduce the n! redudancy of a standard search algorithm.
2. Check constraints as we go – We only consider values that do not conflict previous assignments, thus increasing efficiency. 

### Heuristics implemented

* **Minimum Remaining Value** – Chooses the variable with the fewest legal values.

* **Degree** – Chooses the variable with the most constraints on remaining variables

* **Least Constraining Value** – Prioritizes values that rules out the fewest choices for neighboring variables

* **AC3 Inference** – Reduces the size of the domains by removing any values of x that are not consistent with the constraints between x and y

### Usage

* To run MapTest.py: `python3 MapTest.py`

* To run CircuitBoardTest.py: `python3 CircuitBoardTest.py`

Note: To turn heuristics on or off, set the appropriate heuristic variable in CSPSolver.py to True or False. If no heuristics are turned on, a random variable or value will be generated.
