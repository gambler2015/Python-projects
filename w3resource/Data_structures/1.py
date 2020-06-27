#1. Write a Python program to create an Enum object and display a member name and value. 
"""
Sample data :
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
Antarctica = 672
Expected Output :
Member name: Albania
Member value: 355
"""
import enum
class country(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print("Member name: {}".format(country.Albania.name))
print("Member value: {}".format(country.Albania.value))
