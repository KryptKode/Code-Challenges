import java.util.Scanner; //used to read user input

public class MainClass{

    //main method; program execution begins here
    public static void main(String [] args){
        Scanner userInput = new Scanner(System.in); //instance of the scanner class to get user input

        //prompt the user to enter the data
        System.out.print("Enter a, b, c (separated by SPACES) -->");

        //read the data from the input stream
        double a = userInput.nextDouble();
        double b = userInput.nextDouble();
        double c = userInput.nextDouble();

        //create an instance of the QuadraticEquation class, passing the values of a, b, c entered by the user
        QuadraticEquation instance = new QuadraticEquation(a, b, c);

        //get the value of the discriminant
        double discriminant = instance.getDiscriminant();


        //output the values entered by the user using the getter methods for each attribute
        System.out.println("You entered");
        System.out.println("-->a = " + instance.getA());
        System.out.println("-->b = " + instance.getB());
        System.out.println("-->c = " + instance.getC());

        //if the discriminant is zero (D=0), we have two equal roots, we only need to evaluate one of them
        if (discriminant == 0) {
            System.out.println("The root is " + instance.getRoot1()); //output the root, calling the getRoot1() method in the QuadraticEquation class

        }
        // if the discriminant is greater than zero (D>0), we have two distinct real number roots
        else if (discriminant > 0) {
            System.out.println("The roots are " + instance.getRoot1()

                    + " and " + instance.getRoot2());  //output the roots, calling the getRoot1() and getRoot2() methods in the QuadraticEquation class
        }
        //if the discriminant is negative (D<0), the roots are not real but complex and the code cannot handle complex number
        //so we output no roots
        else {
            System.out.println("The equation has no (real number) roots");

        }
    }

}