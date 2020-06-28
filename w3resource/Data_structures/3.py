# 3. Write a Python program to display all the member name of an enum class ordered by their values.
"""
Expected Output:
Country Name ordered by Country Code:
Afghanistan
Algeria
Angola
Albania
Andorra
Antarctica
"""

import enum
class country(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print([s.name for s in sorted(country)])
