#Write a Python program for binary search for an ordered list.
def binary_search(sequence, item):
    first_index=0
    end_index=len(sequence)-1
    while first_index<=end_index:
        mid_index=first_index+(end_index-first_index)//2
        mid_element=sequence[mid_index]
        if item==mid_element:
            return mid_index
        elif item>mid_element:
            first_index=mid_index+1
        else:
            end_index=mid_index-1
    return None
seq_1=[1,2,3,4,5,6,7,8,9]
item1=3
print(binary_search(seq_1, item1))
