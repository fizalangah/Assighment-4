# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!


def pythagorean():
    ab = float(input("Enter the length of side ab: "))
    ac = float(input("Enter the length of side ac: "))
    bc = (ab**2 + ac**2)**0.5
    print("The length of side bc is", bc)
pythagorean()