# 2. Write a Python program to iterate over an enum class and display individual member and their value.

"""
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
Antarctica = 672
"""
import enum
class country(enum.Enum):
    Afghanistan = 93
    Albania = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
for list1 in country:
    print("{} = {}".format(list1.name, list1.value))
