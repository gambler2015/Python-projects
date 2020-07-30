#Write a Python program for binary search. 
#Binary Search: Search a sorted array by repeatedly dividing
#the search interval in half

   # Compare x with the middle element.
   # If x matches with middle element, we return the mid index.
   # Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
   # Else (x is smaller) recur for the left half.

def binarySearch(sequence, item):
    beg_index=0
    end_index=len(sequence)-1
    while beg_index<=end_index:
        mid_point=beg_index+(end_index-beg_index)//2
        mid_elem=sequence[mid_point]
        if item==mid_elem:
            return mid_point
        elif item<mid_elem:
            end_index=mid_point-1
        else:
            beg_index=mid_point+1
    return None
sequence_1=[10,21,30,40,43,60,101,301,600]
item_1=60
print(binarySearch(sequence_1, item_1))
