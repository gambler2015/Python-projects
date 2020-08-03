#Write a Python program to sort a list of elements using the selection sort algorithm.

# Starting from the first element, we search the smallest element in the 
#array, and replace it with the element in the first position.
#We then move on to the second position, and look for smallest element present 
#in the subarray, starting from index 1, till the last index.
#We replace the element at the second position in the original array, or we 
#can say at the first position in the subarray, with the second smallest 
#element.
# This is repeated, until the array is completely sorted.


def Selection_Sort(list_1):
    for i in range(0, len(list_1)-1):
        min_val=i
        for j in range(i+1, len(list_1)):
            if list_1[j]<list_1[min_val]:
                min_val=j
        if min_val != i:
            list_1[min_val], list_1[i] = list_1[i], list_1[min_val]
    return list_1
list_2=[70,2,60,3,50,20]
print(Selection_Sort(list_2))
