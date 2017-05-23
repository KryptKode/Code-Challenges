# checks if the passed string is a palindrome
def is_palindrome(string):
    # if the string is the same as the reverse of the string, then the string is a palindrome
    if string == string[::-1]:  # string[::-1] gives the reverse of "string"
        return True


# this function checks the passed string for the possible palindromes
#  it returns the longest palindrome and an array of the palindromes
def find_longest_palindrome(string):
    palindromes_arr = [] # this list(array) holds the palindromes

    # these nested loops combines characters in the passed string
    # checks if the character sequence is a palindrome
    # if it is a palindrome, it stores the character sequence in a list (array)
    for i in range(len(string)):  # loop from 0 to the number of characters in the string
        for j in range(0, i):  # loop from 0 to i
            palindrome = string[j:i + 1]  # combine characters from j to i+1
            if is_palindrome(palindrome):  # if  the character sequence is a palindrome, add it to the array
                palindromes_arr.append(palindrome)
    # if there are multiple items of the same size/length, it returns the first one encountered
    return (max(palindromes_arr, key=len)), palindromes_arr # return the longest palindrome and the list of palindromes


# the main function
def main():
    # lines 27- 35 just for designs
    print("*" * 20)
    print ("*   Palindrome!!!  *")
    print("*" * 20)

    print(" "+"_" * 73)
    print("| A palindrome is a word, phrase, number, or other sequence of characters |")
    print("|  which reads the same backward as forward, such as madam or racecar     |")
    print(" " + "_" * 73)

    # ask the user to enter a string
    print("\nTry it out!!!")
    print("Enter a string (no SPACES) and the program will return the longest palindrome in the string")
    user_input = input("-->") # user input is stored here

    # call our function to find the longest palindrome
    # store the longest palindrome in the variable, *longest_palindrome*
    # store the array of palindromes in the variable, *array_of_palindromes*
    longest_palindrome, array_of_palindromes = find_longest_palindrome(user_input)

    # print out the palindromes and state the longest
    print("The possible palindrome(s) in \n" + "*** " + user_input + " ***" )
    print("Are: " + "-->" + ", ".join(array_of_palindromes) + "<--")
    print("The longest palindrome is \n" + "*** " + longest_palindrome + " ***")

if __name__ == '__main__':
    main()