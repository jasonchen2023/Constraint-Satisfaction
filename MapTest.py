# Jason Chen
## CS76 Fall21
## PA 4

from CSPSolver import CSPSolver
from MapColoringCSP import MapColoringCSP

# Test 1: Australia map
print("-----test 1-------")

variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
possible_values = ["r", "g", "b"]

constraint_graph = {"WA": ["NT", "SA"], "NT": ["WA", "SA", "Q"], "SA": ["WA", "NT", "Q", "NSW", "V"], "Q": ["NSW", "NT", "SA"], "NSW": ["Q", "SA", "V"], "V": ["SA", "NSW"], "T":[]}
Australia = MapColoringCSP(variables, possible_values, constraint_graph)

csp = CSPSolver(Australia)

print("assignment", csp.backtracking_search())
print(csp.num_calls)


# Test 2: Australia map with only two possible colors

print("-----test 2-------")

possible_values2 = ["r", "g"]
Australia2 = MapColoringCSP(variables, possible_values2, constraint_graph)
csp2 = CSPSolver(Australia2)

print("assignment", csp2.backtracking_search())
print(csp2.num_calls)


# Test 3: A map of the regions of Canada
print("-----test 3-------")

variables3 = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]

possible_values3 = ["r", "g", "b", "y"]
constraint_graph3 = {"YT":["NT", "BC"], "NT": ["YT", "NU", "MB", "SK", "AB", "BC"], "BC":["YT", "NT", "AB"], "AB": ["BC", "SK", "NT"], "SK": ["NT", "MB", "NU", "AB"], "NU": ["NT", "SK", "MB"], "MB": ["NU", "NT", "SK", "ON"], "ON": ["MB", "QC"], "QC": ["ON", "NL", "NB"], "NL": ["QC"], "NB": ["QC", "NS"], "NS": ["NB"], "PE":[]}

Canada = MapColoringCSP(variables3, possible_values3, constraint_graph3)
csp3 = CSPSolver(Canada)
print("assignment", csp3.backtracking_search())
print(csp3.num_calls)


# Test 4: A map of regions of Canada, but only with 3 valid colors. There is no valid assignment

print("-----test 4-------")

possible_values4 = ["r", "g", "b"]

Canada4 = MapColoringCSP(variables3, possible_values4, constraint_graph3)
csp4 = CSPSolver(Canada4)
print("assignment", csp4.backtracking_search())
print(csp4.num_calls)