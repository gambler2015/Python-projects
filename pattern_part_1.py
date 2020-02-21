"""
 Write a program that prints following shape, (Hint: Use for loop inside another for loop)

    *

    **

    ***    

    ****

    *****

    """

for i in range(0, 5):
    for j in range(0, i+1):
    	print("*",end="")
    print("\n")