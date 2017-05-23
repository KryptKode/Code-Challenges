class QuadraticEquation:

    # constructor for the class
    def __init__(self, a , b, c):
        # private variables for the coefficients of the quadratic equation
        self.a = a
        self.b = b
        self.c = c

    # getter method for variable a
    def getA(self):
        return str(self.a)

    # getter method for variable b
    def getB(self):
        return str(self.b)

    # getter method for variable c
    def getC(self):
        return str(self.c)

    # method to return the discriminant of the equation D = (b^2 - 4ac)
    def getDiscriminant(self):
        discriminant = self.b **2 - (4.0 * self.a * self.c);
        return discriminant

    # method to get the first root r1 = (-b + D^1/2)/2a
    def getRoot1(self):
        root1= (-self.b +(self.getDiscriminant() ** 0.5)) / (2.0 * self.a)
        return str(root1)

    # method to get the second root r2 = (-b - D^1/2)/2a
    def getRoot2(self):
        root2 = (-self.b - (self.getDiscriminant() ** 0.5)) / (2.0 * self.a)
        return str(root2)


# main method; program execution begins here
def main():

    # prompt the user to enter the data
    print("Enter a, b, c (separated by SPACEs)")
    user_input = input("-->") # read the data from the input stream
    a,b,c = (user_input.split(" ")) # store the values in a, b ,c

    # create an instance of the QuadraticEquation class, passing float values of a, b, c entered by the user
    instance = QuadraticEquation(float(a), float(b), float(c))

    # get the value of the discriminant
    discriminant = instance.getDiscriminant()

    # output the values entered by the user using the getter methods for each attribute
    print("You entered")
    print("-->a = " + instance.getA())
    print("-->b = " + instance.getB())
    print("-->c = " + instance.getC())

    # if the discriminant is zero (D=0), we have two equal roots, we only need to evaluate one of them
    if discriminant == 0:
        #  output the root, calling the getRoot1() method in the QuadraticEquation class
        print("The root is " + instance.getRoot1())

    # if the discriminant is greater than zero (D > 0), we have two distinct real number roots
    elif discriminant > 0:
        # output the roots, calling the getRoot1() and getRoot2() methods in the QuadraticEquation class
        print("The roots are " + instance.getRoot1() + " and " + instance.getRoot2())

    # if the discriminant is negative (D<0), the roots are not real but complex
    # and the code cannot handle complex number
    # so we output no roots
    else:
        print("The equation has no (real number) roots")

# run the main function if the file is not loaded as a module
if __name__ == '__main__':
    main()