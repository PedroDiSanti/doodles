# Check Range
# accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit; (IRRELEVANT)
# if the user enters a string that is not an integer value, the function should emit the message
    ## Error: wrong input, and ask the user to input the value again; ##
# if the user enters a number which falls outside the specified range, the function should emit the message
    ## Error: the value is not within permitted range (min..max) and ask the user to input the value again; ##
# if the input value is valid, return it as a result.

MIN = -10
MAX = 10


def read_int(prompt) -> bool:
    try:
        value = int(prompt)
        if MIN >= value or value <= MAX:
            print("The number is:", value)
        else:
            print("Error: the value is not within permitted range (-10..10)")
    except ValueError:
        print("Error: wrong input")


if __name__ == '__main__':
    number_in_str = input("Enter a number from -10 to 10: ")
    result = read_int(number_in_str)
