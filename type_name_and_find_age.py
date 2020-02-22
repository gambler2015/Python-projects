"""
 Write python program that allows to store age of your family members.
 Program should ask to enter person name and age and once you are done
 you should be able to input name of the person and program should tell 
 the age. Now print name of all your family members along with their ages.
"""

details={"Aziz":24, "Saif": 28, "Asad":35, "Abdullah":31, "Firoza":44, "Samima":40}
name=input()
print("Age of this person is:", details[name])
print(details)