# Quadratic Eqaution solver in Python

This program illustrates object-oriented programmin concept by solving a quadratic equation

## Quick Notes
In algebra, a quadratic equation (from the Latin quadratus for "square") is any equation having the form
	```
		ax^2+bx+c=0
	```
where x represents an unknown, and a, b, and c represent known numbers such that a is not equal to 0. 
If a = 0, then the equation is linear, not quadratic. 
The numbers a, b, and c are the coefficients of the equation, and may be distinguished by calling them, respectively, the quadratic coefficient, the linear coefficient and the constant or free term.
```
	This program gives results for quadratic equations with real roots only... 
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need any working version of Python 3 installed on your system


### Installing

A step-by-step guide on how to install Python 3 on Windows is shown in this link
The same process goes using a mac.


http://tecadmin.net/install-python-3-windows




## Procedure to run the program

* Open QuadraticEqaution.py in IDLE by right clicking on it an selecting "Edit with IDLE"
* Run it either by pressing F5 key or by clicking >Run >Run Module on the menu tabs

```
When the program runs, it asks for the values of a, b, c. Enter the values seperated by SPACES
```
Example: 1 5 6
```
Output:
Enter a, b, c (separated by SPACEs)
-->1 5 6
You entered
-->a = 1.0
-->b = 5.0
-->c = 6.0
The roots are -2.0 and -3.0
```
### How it works
* The class QuadraticEquation is defined
* The constructor initializes the variables (a, b, c)
* Getter methods for each of the variables are defined
* The method to calculate the discriminant, D is defined D = (b^2 - 4ac)
* The methods to get the roots of the equation are defined
* In main function, the user is asked to enter values for a, b, c and the roots are evaluated
**For more detailed explanation, refer to the comments in the source code**


## Built With

* Python 3 (http://www.python.org)

## Resources
* Wikipedia - (https://en.wikipedia.org/wiki/Quadratic_equation) for definition of Quadratic Equation

## Authors

* **Paul A.** - *Cyberman*(https://github.com/KryptKode)


## Acknowledgments

* Thanks to Prodsters team...
* Thanks to Mr. Smatt for inititing the challenge
* Thanks to God for life
