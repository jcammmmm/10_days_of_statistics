
# A Python program to print all  
# permutations using library function 
from itertools import permutations 
  
# Get all permutations of [1, 2, 3] 
l1 = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
l2 = ['A', 'B', 'C', 'D', 'E']
perm = permutations(l2) 
  
# Print the obtained permutations
for i in list(perm): 
    print(*i)
