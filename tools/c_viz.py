
# A Python program to print all  
# combinations of given length 
from itertools import combinations 
  
# Get all combinations of [1, 2, 3] 
# and length 2 
comb = combinations(['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], 2) 
  
# Print the obtained combinations 
for i in list(comb): 
    print(*i, sep=' ') 
