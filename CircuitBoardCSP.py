# Jason Chen
## CS76 Fall21
## PA 4

import math
from collections import deque

class CircuitBoard:

    def __init__(self, width, height, components):
        self.board_width = width
        self.board_height = height

        self.variables = list(range(0, int(len(components)/2)))    # components numbered and stored in a list

        # stores the width and height of each piece
        self.components_dict = {}
        for i in range(0, len(components), 2):
            self.components_dict[int(i/2)] = (components[i], components[i+1])

        self.domains = {}   # dictionary tracking possible locations for each piece
        self.build_domains()

        self.constraints = {}   # stores binary constraints
        for i in self.variables:
            for j in set(self.variables) - {i}:
                self.constraints[(i, j)] = self.find_possible_locations(i, j)



    # builds the domain of each variable. Domain includes all locations where the component fits on board
    def build_domains(self):
        for var in self.components_dict:

            self.domains[var] = []

            for x in range(0, self.board_width):    # loop through every location on board
                for y in range(0, self.board_height):
                        
                    w, h = self.components_dict[var][0], self.components_dict[var][1]
                    
                    if x + w <= self.board_width and y + h <= self.board_height:  # component fit on board
                        self.domains[var].append((x, y))


    # finds the possible locations for two components such that they do not overlap
    def find_possible_locations(self, i, j):
        possible_locations = []
        for location_i in self.domains[i]:
            for location_j in self.domains[j]:
                if not self.is_overlapping(i, j, location_i[0], location_i[1], location_j[0], location_j[1]):
                    possible_locations.append((location_i, location_j))
        return possible_locations


    # Used by degree heuristic. Returns area of the component as that is a good proxy for how many constraints that component imposes
    def get_num_constraints(self, var):
        return self.components_dict[var][0] * self.components_dict[var][1]
    

    # returns whether we can rule out neighbor's value
    def rule_out(self, var, nbr, value, nbr_value):
        return self.is_overlapping(var, nbr, value[0], value[1], nbr_value[0], nbr_value[1])


    # returns true if two components overlap
    def is_overlapping(self, var, nbr, x1, y1, x2, y2):

        d = self.components_dict

        if x1 >= x2 + d[nbr][0] or x1 + d[var][0] <= x2 or y1 >= y2 + d[nbr][1] or y1 + d[var][1] <= y2:    # no components overlap
            return False
        else:
            return True


        # returns true if an assignment is consistent i.e. does not overlap with other components
    def is_consistent(self, var, value, assignment):

        for assigned in set(assignment) - {var}:
            if (value, assignment[assigned]) not in self.constraints[(var, assigned)]:
                return False

        return True
                

    # prints the board given an assignment
    def print_board(self, assignment):

        if assignment == False:
            return

        for y in range(self.board_height - 1, -1 , -1):
            for x in range(0, self.board_width):

                empty = True

                for c in assignment:
                    if self.has_component(c, assignment[c][0], assignment[c][1], x, y):
                        print(chr(c + 97), end = "")
                        empty = False
                if empty == True:
                    print(".", end="")                
                
            print("")


    # Used by print_board. Returns whether there is a component in a location on the board
    def has_component(self, c, x1, y1, x2, y2):
        d = self.components_dict
        if x1 > x2 or x1 + d[c][0] <= x2 or y1 > y2 or y1 + d[c][1] <= y2:    # no component in that location
            return False
        return True

    # returns true if assignment is complete
    def goal_test(self, assignment):
        return len(assignment) == len(self.variables)


    