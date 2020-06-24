#To print out the entire two dimensional array we can use python for loop as shown below. We use end of line to print out the values in different rows.

from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
for r in T:
    for c in r:
        print(c,end = " ")
    print()
# When the above code is executed, it produces the following result −

# 11 12 5 2 
# 15 6 10 
# 10 8 12 5 
# 12 15 8 6 
