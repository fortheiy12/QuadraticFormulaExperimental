import cmath
import math


def Start():
    formChoice = str(input("Vertex Form or Standard Form? ")).strip()
    if formChoice == "Standard" or formChoice == "s" or formChoice == "standard" or formChoice == "Standard Form" or formChoice == "standard form":
        calculateStandardform()
    elif formChoice == "Vertex" or formChoice == "v" or formChoice == "vertex" or formChoice == "Vertex Form" or formChoice == "vertex form":
        calculateVertexform()
    else:
        Start()


def contFunc():
    contPrompt = input("Would you like to do an additional calculation?" +
                       "\n" + "Yes or No? ")
    if contPrompt == "Yes" or contPrompt == "y":
        Start()
    else:
        contFunc()


def calculateStandardform():
    inequalityPresent = ""
    print("Please make sure the equation you are gathering A, B, and C are in ax^2+bx+c=0, and also seperate your inputs by using a comma and a space.")
    try:
        a, b, c = input("A, B, C ").split(", ")
    except ValueError:
        calculateStandardform()
        return
    roundTo = int(input("Places to round to? "))
    inequality = input("Is the inequality greater than, less than, or equal to? ")
    if inequality == "<=":
        inequalityPresent = "lessThanequal"
    elif inequality == ">=":
        inequalityPresent = "greaterThanequal"
    elif inequality == "<":
        inequalityPresent = "lessThan"
    elif inequality == ">":
        inequalityPresent = "greaterThan"
    elif inequality == "=":
        inequalityPresent = "equal"
    else:
        return
    a = float(a)
    b = float(b)
    c = float(c)
    firstpart = -b
    discriminant = b**2 - 4 * a * c
    denomintor = 2 * a
    try:
        sqrted = math.sqrt(discriminant)
    except ValueError:
        print("This equation has no real roots.")
        askUsercon = input(
            "Would you like to restart this calculation with the discriminant dealt with by cmath?"
            + "\n" + "Yes or No? ")
        if askUsercon == "Yes" or askUsercon == "y":
            specialCalculatestandard(a, b, c, roundTo)
        else:
            exit()
        return
    numerator1 = firstpart + sqrted
    numerator2 = firstpart - sqrted
    sum1 = numerator1 / denomintor
    sum2 = numerator2 / denomintor
    
    print("Answer 1: " + str(round(sum1, roundTo)) + inequalityPresent)
    if sum2 != sum1 or sum2 == 0:
        print("Answer 2: " + str(round(sum2, roundTo)) + inequalityPresent)
        contFunc()
    else:
        contFunc()


def calculateVertexform():
    try:
        print("Please make sure the equation you are gathering A, B, and C are in a(x+h)^2+k=y, and also seperate your inputs by using a comma and a space.")
    except ValueError:
        calculateVertexform()
        return
    a, h, k, y = input("A, H, K, Y ").split(", ")
    roundTo = int(input("Places to round to? "))
    inequality = input("Is the inequality greater than, less than, or equal to? ")
    if inequality == "<=":
        inequalityPresent = "lessThanequal"
    elif inequality == ">=":
        inequalityPresent = "greaterThanequal"
    elif inequality == "<":
        inequalityPresent = "lessThan"
    elif inequality == ">":
        inequalityPresent = "greaterThan"
    elif inequality == "=":
        inequalityPresent = "equal"
    else:
        return
    a = float(a)
    h = float(h)
    k = float(k)
    y = float(y)
    if k < 0:
        y = y + -k
    elif k > 0:
        y = y - k
    else:
        y = y
    y = y / a if a != 1 else y
    try:
        root1 = math.sqrt(y)
    except ValueError:
        print("This equation has no real roots.")
        askUsercon = input(
            "Would you like to restart this calculation with the discriminant dealt with by cmath?"
            + "\n" + "Yes or No? ")
        if askUsercon == "Yes" or askUsercon == "y":
            specialCalculatevertex(a, h, k, y, roundTo)
        else:
            exit()
        return
    root2 = -root1
    if h < 0:
        root1 = root1 + -h
        root2 = root2 + -h
    else:
        root1 = root1 - h
        root2 = root2 - h
        print("Answer 1: " + str(round(root1, roundTo)) + inequalityPresent)
        if root2 != root1:
            print("Answer 2: " + str(round(root2, roundTo)) + inequalityPresent)
            contFunc()
        else:
            contFunc()


def specialCalculatestandard(a, b, c, roundTo):
    a = float(a)
    b = float(b)
    c = float(c)
    firstpart = -b
    discriminant = b**2 - 4 * a * c
    denomintor = 2 * a
    sqrted = cmath.sqrt(discriminant)
    numerator1 = firstpart + sqrted
    numerator2 = firstpart - sqrted
    sum1 = numerator1 / denomintor
    sum2 = numerator2 / denomintor
    print("Answer 1: " + str(round(sum1.imag, roundTo)) + "i")
    print("Answer 1: " + str(round(sum1.real, roundTo)) + " Real Part")
    if sum2 != sum1 or sum2 == 0:
        print("Answer 2: " + str(round(sum2.imag, roundTo)) + "i")
        print("Answer 2: " + str(round(sum2.real, roundTo)) + " Real Part")
        contFunc()
    else:
        contFunc()


def specialCalculatevertex(a, h, k, y, roundTo):
    a = float(a)
    h = float(h)
    k = float(k)
    y = float(y)
    if k < 0:
        y = y + -k
    elif k > 0:
        y = y - k
    else:
        y = y
    y = y / a if a != 1 else y
    root1 = cmath.sqrt(y)
    root2 = -root1
    if h < 0:
        root1 = root1 + -h
        root2 = root2 + -h
    else:
        root1 = root1 - h
        root2 = root2 - h
    print("Answer 1: " + str(round(root1.imag, roundTo)) + "i")
    print("Answer 1: " + str(round(root1.real, roundTo)) + " Real Part")
    if root2 != root1 or root2 == 0:
        print("Answer 2: " + str(round(root2.imag, roundTo)) + "i")
        print("Answer 2: " + str(round(root2.real, roundTo)) + " Real Part")
        contFunc()
    else:
        contFunc()


Start()
