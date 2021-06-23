import sys
from functions import display_file

def main():
    """
    Program takes in one file argument from the command line and prints details
    """
    if(len(sys.argv) == 2):
        try:
            input_file = open(str(sys.argv[1]), "r")
            if input_file:
                display_file(input_file)
            else:
                print("invalid filename: badfile")
        except FileNotFoundError:
            print("invalid filename: badfile")
    else:
        print("usage: python3 file_reading filename")

if __name__ == "__main__":
    main()