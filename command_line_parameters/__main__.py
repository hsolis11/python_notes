import sys
from functions import string_length


def main():
    """
    Reads argv from command line and prints the character count of each argument
    """

    print("My command line analyzer...")
    print("The number of command line parameters are: ", len(sys.argv))
    print("The length of the name of the program is: ", string_length(sys.argv[0]))

    if(len(sys.argv) > 1):
        for i in range(len(sys.argv)):
            print(f"The length of the paramter {i} is {string_length(sys.argv[i])} ")


if __name__ == '__main__':
    main()

