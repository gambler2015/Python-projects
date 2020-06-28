#5. Write a Python program to count the most common words in a dictionary.
#Expected Output:
#[('pink', 6), ('black', 5), ('white', 5), ('red', 4)]

words = [
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red'
]
"""
d=[]
for i in words:
    if i in d:
        continue
    else:
        d.append(i)
print(d)
"""
from collections import Counter
word_counts=Counter(words)
print(word_counts)
top_four=word_counts.most_common(4)
print("most common words")
print(top_four)
