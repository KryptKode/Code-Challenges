# MorseTextConverter in Python

This program can covert plain english text to morse code and vice versa

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need any working version of Python 3 installed on your system


### Installing

A step-by-step guide on how to install Python 3 on Windows is shown in this link
The same process goes using a mac.
```
https://techadmin.net/install-python-3-windows/
```


## Procedure to run the program

*Open MorseTextConverter.py in IDLE by right clicking on it an selecting "Edit with IDLE"
*Run it either by pressing F5 key or by clicking >Run >Run Module on the menu tabs

```
When you want to *decode* to plain text from a morse code, 
enter the morse code of each letter seperated by a pipe character "|"
Seperate each word with a space
```
Example: --.|---|-..| |-...|.-..|.|...|...| |...|--|.-|-|-|
```
Only with this format can the program decrypt your morse code
```
### How it works
*In the program,
*The class MorseTextConverter is created and 
*The plain text morse codes are stored as key-value pairs in a dictionary type
*Another reverse dictionary is created by reversing the key-value pair on the first dictionary file
*Two methods - @returns morseToText(@params) and @returns textToMorse(@params) are defined in the class
*The methods take a string parameter and also return a string
*In the morseToText() method, the sting value is converted to an array, stripping all the non_morse code parts (line71-73)
*Each item in the array is then mapped with the dictionary containing the key-value pairs of the codes
*Finally, the array is converted to a string
*In the textToMorse() method, 
*each character in the string passed as a parameter is compared with the dictionary file
*The resulting encoded string is returned


## Built With

* Python 3

##Resources
*Wikipedia - (http://wikipedia.org) for the morce codes

## Authors

* **Paul A.** - *Cyberman*(https://github.com/cyberman09)


## Acknowledgments

* Thanks to Prodsters team..
* Thanks to Mr. Smatt for inititing the challenge
* Thanks to God for life

