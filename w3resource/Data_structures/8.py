# 8.Write a Python program to get the unique enumeration values.
"""
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
"""
from enum import Enum
class country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
for i in country:
    print("{:15} = {}".format(i.name, i.value))
