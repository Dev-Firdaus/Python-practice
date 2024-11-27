"""
111
111
111
"""
"""
for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")
    print()
"""
for i in range(5):  # Outer loop for rows
    # Print spaces
    for j in range(i):
        print(" ", end="")
    # Print numbers
    for k in range(5, i, -1):
        print(k, end="")
    print()  # Move to the next line

