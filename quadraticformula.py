import cmath
import math



def contFunc():
    contPrompt = input("Would you like to do an additional calculation?" +
                       "\n" + "Yes or No? ")
    if contPrompt == "Yes":
        Calculate()
    else:
        exit()


def Calculate():
    formChoice = input("Vertex or Standard? ")
    if formChoice == "Standard":
        a, b, c = input("A, B, C ").split(", ")
        roundTo = int(input("Places to round to? "))
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
            if askUsercon == "Yes":
                specialCalculatestandard(a, b, c, roundTo)
            else:
                exit()
            return
        numerator1 = firstpart + sqrted
        numerator2 = firstpart - sqrted
        sum1 = numerator1 / denomintor
        sum2 = numerator2 / denomintor
        print("Answer 1: " + str(round(sum1, roundTo)))
        if sum2 != sum1 or sum2 == 0:
            print("Answer 2: " + str(round(sum2, roundTo)))
            contFunc()
        else:
            contFunc()
    elif (formChoice == "Vertex"):
        a, h, k, y = input("A, H, K, Y ").split(", ")

        roundTo = int(input("Places to round to? "))
        
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
            if askUsercon == "Yes":
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
        print("Answer 1: " + str(round(root1, roundTo)))
        if root2 != root1:
            print("Answer 2: " + str(round(root2, roundTo)))
            contFunc()
        else:
            contFunc()
    elif formChoice == "Factored":
        print("Figure it out.")


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
    print("Answer 1: " + str(round(sum1.imag, roundTo)) + str("i"))
    if sum2 != sum1 or sum2 == 0:
        print("Answer 2: " + str(round(sum2.imag, roundTo)) + "i")
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
    if root2 != root1 or root2 == 0:
        print("Answer 2: " + str(round(root2.imag, roundTo)) + "i")
        contFunc()
    else:
        contFunc()


Calculate()
