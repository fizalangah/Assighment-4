# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.


def feet():
    inches_per_foot = 12
    feet = float(input("Enter the number of feet: "))
    inches = feet * inches_per_foot
    print(feet, "feet is", inches, "inches.")
feet()    