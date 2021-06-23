import sys
from functions import *

def main():
    if len(sys.argv) == 2:
        
        if is_positive_integer(int(sys.argv[1])):

            SIZE = int(sys.argv[1])

            numbers1 = []
            numbers2 = []
            answer = []

            fill_random(numbers1, SIZE)
            fill_random(numbers2, SIZE)

            print("The two arrays created are:")
            display_array(numbers1, SIZE)
            display_array(numbers2, SIZE)

            print('\n')

            print("Adding the arrays together:")
            add_arrays(answer, numbers1, numbers2, SIZE)
            display_array(answer, SIZE)

            print('\n')

            print("The sum and avg of the arrays:")
            print(f"array 1 sum: {sum_array(numbers1, SIZE)}")
            print(f"array 1 average: {avg_array(numbers1, SIZE)}")

            print(f"array 2 sum: {sum_array(numbers2, SIZE)}")
            print(f"array 2 average: {avg_array(numbers2, SIZE)}")
        else:
            print("usage: python3 arrays n (where n is a number above 0)")    
    else:
        print("usage: python3 arrays n (where n is a number above 0)")

if __name__ == '__main__':
    main()