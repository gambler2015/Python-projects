#Write a Python program for sequential search.
#In computer science, linear search or sequential search is a method for
#finding a particular value in a list that checks each element in sequence
#until the desired element is found or the list is exhausted.
#The list need not be ordered.
def sequential_search(sequential, item):
    position=0
    while position<len(sequential):
        if sequential[position]==item:
            return position
        position = position+1
    return False
sequential_1=[20, 30,32,43,54,71,83,91,99,109,122,130]
item_1=99
print(sequential_search(sequential_1, item_1))
