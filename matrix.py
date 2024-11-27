
#-------------

for i in range(5):  # Outer loop for rows
    # Print spaces
    for j in range(i):
        print(" ", end="")
    # Print numbers
    for k in range(5, i, -1):
        print(k, end="")
    print()  # Move to the next line

#----------

for i in range(1,4):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
#----------
n=1
for i in range(1,4):
    for j in range(1,4):
        print(chr(n+64),end=" ")
        n=n+1
    print()