# Jason Chen
## CS76 Fall21
## PA 4

from CircuitBoardCSP import CircuitBoard
from CSPSolver import CSPSolver

# standard board given in assignment
print("------- Test 1 -------")
cb1 = CircuitBoard(10, 3, (3, 2, 5, 2, 2, 3, 7, 1))
csp1 = CSPSolver(cb1)

assignment = csp1.backtracking_search()

print("assignment", assignment)

cb1.print_board(assignment)
print("num_calls", csp1.num_calls)

# 10x15 board
print("------- Test 2 -------")

cb2 = CircuitBoard(10, 15, (3, 2, 5, 2, 2, 3, 7, 1, 8, 3, 2, 6, 5, 2, 9, 2, 3, 2, 4, 1, 2, 5, 1, 4))
csp2 = CSPSolver(cb2)

assignment2 = csp2.backtracking_search()
print("assignment", assignment2)
cb2.print_board(assignment2)
print("num_calls", csp2.num_calls)


print("------- Test 3 -------")

# Test: 10x3 board, pieces larger than board

cb3 = CircuitBoard(10, 3, (3, 2, 5, 2, 2, 3, 7, 1, 8, 4, 2, 4))
csp3 = CSPSolver(cb3)

assignment3 = csp3.backtracking_search()

print("assignment", assignment3)
print("num_calls:", csp3.num_calls)


# Test 4: 10x3 board, pieces do not fit on board

print("------- Test 4 -------")

cb4 = CircuitBoard(10, 3, (3, 2, 5, 2, 2, 3, 7, 1, 8, 3, 2, 2))
csp4 = CSPSolver(cb4)

assignment4 = csp4.backtracking_search()

print("assignment", assignment4)
cb4.print_board(assignment4)
print("num_calls:", csp4.num_calls)


# Test 5: Large 20x30 board
print("------- Test 5 --------")

cb5 = CircuitBoard(20, 30, (3, 2, 5, 2, 2, 3, 7, 1, 8, 3, 2, 2, 12, 3, 5, 6, 9, 2, 2, 10, 12, 10, 8, 8, 12, 2, 3, 7, 6, 6))
csp5 = CSPSolver(cb5)

assignment5 = csp5.backtracking_search()

print("assignment", assignment5)
cb5.print_board(assignment5)
print("num_calls:", csp5.num_calls)