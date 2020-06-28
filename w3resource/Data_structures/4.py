#4. Write a Python program to get all values from an enum class.
#Expected output:
#[93, 355, 213, 376, 244, 672]


from enum import Enum, IntEnum
"""
class country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
list1=[]
for i in country:
    #print(i.name)
    #print(i.value)
    list1.append(i.value)
#print(list(country.value))
print(list1)
"""
class country(IntEnum):
        Afghanistan = 93
        Albania = 355
        Algeria = 213
        Andorra = 376
        Angola = 244
        Antarctica = 672
print(list(map(int,country)))
