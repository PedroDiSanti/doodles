# Digit of life
# asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually,
# the order of the digits doesn't matter) outputs the Digit of Life for the date.

def digit_of_life(date_to_sum: int) -> int:
    date_to_sum_as_str = str(date_to_sum)

    sum_of_int = 0
    sum_is_one_digit = True
    while sum_is_one_digit:
        for number in date_to_sum_as_str:
            sum_of_int += int(number)

        if sum_of_int > 10:
            date_to_sum_as_str = str(sum_of_int)
            sum_of_int = 0
        else:
            sum_is_one_digit = False
    return sum_of_int


if __name__ == '__main__':
    date_to_check = 19991229
    result = digit_of_life(date_to_check)
    print(result)

    date_to_check = 20000101
    result = digit_of_life(date_to_check)
    print(result)
