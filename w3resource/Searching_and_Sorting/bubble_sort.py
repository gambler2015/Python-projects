#Write a Python program to sort a list of elements using the bubble sort algorithm.
#each pair of adjacent elements is compared and the elements are swapped 
#if they are not in order. This algorithm is not suitable for large data 
#sets as its average and worst case complexity are of Ο(n2) where n is the
#number of items.

def Bubble_Sort(list_1):
    for j in range(0, len(list_1)-1):
        for i in range(0, len(list_1)-1):
            if list_1[i]>list_1[i+1]:
                list_1[i], list_1[i+1]=list_1[i+1], list_1[i]
    return list_1
list2=[10,3,2,6,20,7,-20,0,0,3]
print(Bubble_Sort(list2))
