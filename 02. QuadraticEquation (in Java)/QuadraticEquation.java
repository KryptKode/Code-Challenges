/**
 * Created by Cyberman on 5/23/2017.
 */
public class QuadraticEquation {

    //private variables for the coefficients of the quadratic equation
    private double a;
    private double b;
    private double c;

    //constructor for the class
    public QuadraticEquation(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    //getter method for variable a
    public double getA() {
        return a;
    }
    //getter method for variable b
    public double getB() {
        return b;
    }

    //getter method for variable c
    public double getC() {
        return c;
    }

    //method to return the discriminant of the equation D = (b^2 - 4ac)
    public double getDiscriminant(){
        double discriminant = b * b - 4.0 * a * c;

        return discriminant;
    }

    //method to get the first root r1 = (-b + D^1/2)/2a
    public double getRoot1(){
        double root1 = (-b + Math.pow(getDiscriminant(), 0.5)) / (2.0 * a);
        return root1;
    }

    //method to get the second root r2 = (-b - D^1/2)/2a
    public double getRoot2(){
        double root2 = (-b - Math.pow(getDiscriminant(), 0.5)) / (2.0 * a);
        return root2;
    }
}