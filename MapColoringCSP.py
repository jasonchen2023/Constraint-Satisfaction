# Jason Chen
## CS76 Fall21
## PA 4

import math
from collections import deque

class MapColoringCSP:
    def __init__(self, variables, possible_domain, constraints_graph):

        self.variables = variables  # stores all the variables
        self.possible_domain = possible_domain
        self.constraints_graph = constraints_graph  # constraint graph tracking the neighbors of each variable


        self.domains = {}   # tracks the updated domain of each variable

        for var in variables:
            self.domains[var] = self.possible_domain.copy()


        self.constraints = {}   # stores binary constraints

        color_constraints = self.build_constraints()        

        for var in constraints_graph:
            for nbr in constraints_graph[var]:
                self.constraints[(var, nbr)] = color_constraints

        # print(self.constraints)


    # builds all combinations of colors that satisfy constraint
    def build_constraints(self):

        l = []

        # print("possible domain", self.possible_domain)

        for color1 in self.possible_domain:
            for color2 in set(self.possible_domain) - {color1}:
                l.append((color1, color2))
        
        return l


    # returns number of neighbors the region has
    def get_num_constraints(self, var):
        return len(self.constraints_graph[var])


    # returns true if an assignment is consistent
    def is_consistent(self, var, value, assignment):

        for assigned in set(assignment) - {var}:
            if assigned in self.constraints_graph[var]:
                if (value, assignment[assigned]) not in self.constraints[(var, assigned)]:
                    return False
            
        return True

    # returns True if assignment is complete
    def goal_test(self, assignment):
        return len(assignment) == len(self.variables)

    # returns True if we can rule out a value
    def rule_out(self, var, nbr, value, nbr_value):
        return value == nbr_value
