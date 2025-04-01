# It is used to store data values in pair key:value 
# They are Unordered means there is no index like tupple list and strings
# Mutable(changable)
# Don't follw duplicate keys One key name at a time

Info = {
    "Key" : "value",
    "name" : "Vishwajit",
    "cgpa" : 8.95,
    "marks" : [86,56,54,78,90],
}

# print(Info["name"])
# Info["surname"] = "kamble"
# Info["name"] = "Vishu"
# print(Info["name"])
# print(Info)

# Nested Dictionary
student = {
    "name" : "Vishwajit Kamble",
    "subjects" : {
        "phy" : 67,
        "chem" : 89,
        "math" : 100
    }
} 

print(student["subjects"]["chem"])