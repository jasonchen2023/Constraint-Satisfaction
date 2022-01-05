
# Jason Chen
## CS76 Fall21
## PA 4

import math
import random
from collections import deque
import copy

class CSPSolver:

    def __init__(self, csp_problem):

        self.csp = csp_problem

        # heuristics: Set to True for on, False for off
        self.run_MRV = False
        self.run_degree = True
        self.run_LCV = True
        self.run_AC_3 = False

        self.domains = self.csp.domains
  
        self.num_calls = 0
        self.depth = 0


    def backtracking_search(self):

        # check that a solution is indeed possible
        for var in self.csp.constraints:
            if len(self.csp.constraints[var]) == 0:
                return False

        return self.rec_backtracking({}, self.csp)


    # helper function
    def rec_backtracking(self, assignment, csp):

        self.num_calls += 1
        # self.depth += 1

        # if assignment is complete return assignment
        if csp.goal_test(assignment):
            return assignment

        var = self.select_unassigned_var(csp, assignment)
        # print("selected ", var, flush=True)

        for value in self.order_domain_values(var, assignment, csp):

            if csp.is_consistent(var, value, assignment):

                temp_domain = copy.deepcopy(self.domains)   # store a version of current domain dictionary in case assignment does not work out  

                assignment[var] = value     # add {var, value} to assignment
                self.domains[var] = [value]

                # run AC3
                if self.run_AC_3 == True:   
                    result = self.AC_3(csp)

                    if not result:  # early detection of failure, delete assignment
                        del assignment[var]
                        self.domains = temp_domain
                        continue

                    else:   # check if solution is found (only one element in domain for all variables)
                        solution_found = True

                        for v in self.domains:
                            if len(self.domains[v]) != 1:
                                solution_found = False
                        
                        if solution_found == True:  # solution found by AC-3
                            for v in self.domains:
                                assignment[v] = self.domains[v][0]
                            return assignment


                result = self.rec_backtracking(assignment, csp)

                if result != False: # assignment found
                    return result
                
                # delete the assignment and restore the original domain in the dictionary
                del assignment[var]
                self.domains = temp_domain
        
        return False

    # returns an unassigned variable
    def select_unassigned_var(self, csp, assignment):
        
        # Choose the variable with the fewest legal values
        if self.run_MRV == True:
            return self.MRV()

        # Choose the variable with most constraints
        elif self.run_degree == True:
            return self.degree(csp, self.domains)

        else:   # return random variable
            return random.choice(list(set(csp.variables) - set(assignment)))

    
    # returns a list of values in the variable's domain
    def order_domain_values(self, var, assignment, csp):
        
        if self.run_LCV == True:    # run LCV
            return self.LCV(var, csp)
        
        else:   # return random order of list
            values_list = self.domains[var].copy()
            random.shuffle(values_list)
            return values_list

# function AC-3(csp) returns false if an inconsistency is found and true otherwise
    def AC_3(self, csp):
        d = deque()

        # add all the arcs
        for tup in csp.constraints: 
            d.append(tup)


        while len(d) > 0:
            (x, y) = d.popleft()
            if self.revise(csp, x, y):

                if len(self.domains[x]) == 0:   # no values in domain
                    return False

                for tup in csp.constraints:     # add the reversed arc since domain was revised
                    if (tup[1] == x and tup[0] != y):
                        d.append(tup)
        
        return True


    # helper function for AC3. Returns whether domain has been revised or not
    def revise(self, csp, x, y):

        revised = False

        for value_x in self.domains[x]:
            satisfied = False

            # check if there is a value in domain of y that satisfies the constraint between x and y
            for value_y in self.domains[y]:

                if (value_x, value_y) in csp.constraints[(x, y)]:
                    satisfied = True
                    break

            if satisfied == False:  # constraint not satisfied, delete value from domain
                self.domains[x].remove(value_x)
                revised = True

        return revised
        

    # Choose the variable with the fewest legal values
    def MRV(self):

        l = []
        min_values = math.inf

        for var in self.domains:

            if len(self.domains[var]) == 1: # skip assigned variables
                continue    
            elif len(self.domains[var]) == min_values:    # variable has tied-for-fewest legal values
                l.append(var)
            elif len(self.domains[var]) < min_values:   # variable has fewest legal values

                min_values = len(self.domains[var])
                l = [var]

        if len(l) == 1:
            return l[0]

        elif len(l) > 1:  # multiple countries with fewest legal values. Run degree as tie breaker
            return self.degree(self.csp, l)


    # choose the variable with the most constraints on remaining variables
    def degree(self, csp, variables):

        max_constraints = -math.inf
        v = None

        for var in variables:

            if len(self.domains[var]) > 1:    # variable not yet assignment

                num_constraints = csp.get_num_constraints(var)

                if num_constraints > max_constraints:   # greater number of constraints
                    max_constraints = num_constraints
                    v = var

        return v


    # order values that rules out the fewest to most values in the remaining variables
    def LCV(self, var, csp):

        d = {}  # key will be a value in the variable's domain, value will be the number of values "ruled out"

        for var_value in self.domains[var]:   # for each possible location in domain

            ruled_out = 0

            # find the number of ruled out values for every neighbor
            for nbr in set(self.domains) - {var}:

                for nbr_value in self.domains[nbr]:    # loop through every possible location of that neighbor

                    if csp.rule_out(var, nbr, var_value, nbr_value):
                        ruled_out += 1
            
            d[var_value] = ruled_out    # store ruled_out in dictionary 

        ordered_values = sorted(d.keys(), key=d.get)
        return ordered_values
