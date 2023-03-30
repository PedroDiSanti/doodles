# Sudoku
# each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
# each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
# each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
from typing import List

TOTAL = 9
SUBSET = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def treat_string(sudoku_to_be_checked: str) -> str:
    return sudoku_to_be_checked.replace(" ", "").replace("\n", "")


def mount_sudoku_matrix(count_line, matrix, new_line, sudoku_to_be_checked):
    string_to_loop = treat_string(sudoku_to_be_checked)
    for char in string_to_loop:
        if count_line < TOTAL:
            new_line.append(char)
            count_line += 1
        else:
            matrix.append(new_line)
            new_line = [char]
            count_line = 1
    matrix.append(new_line)
    return matrix


def check_sudoku(sudoku_to_be_checked: str) -> List[list]:
    matrix = []
    new_line = []
    count_line = 0

    sudoku_matrix = mount_sudoku_matrix(count_line, matrix, new_line, sudoku_to_be_checked)

    lines_result = check_matrix_lines(sudoku_matrix)
    columns_result = check_matrix_columns(sudoku_matrix)
    three_by_three_result = check_matrix_3_x_3(sudoku_matrix)

    if lines_result and columns_result and three_by_three_result:
        return True
    return False


def check_matrix_lines(sudoku_matrix):
    in_line = inside_line = 0
    while in_line < TOTAL - 1:

        numbers_to_be_checked = []
        while inside_line < TOTAL:
            numbers_to_be_checked.append(int(sudoku_matrix[in_line][inside_line]))
            inside_line += 1
        inside_line = 0

        numbers_to_be_checked.sort()
        if not len(list(set(numbers_to_be_checked) & set(SUBSET))) == 9:
            return False
        in_line += 1
    return True


def check_matrix_columns(sudoku_matrix):
    in_line = inside_line = 0
    while in_line < TOTAL - 1:

        numbers_to_be_checked = []
        while inside_line < TOTAL:
            numbers_to_be_checked.append(int(sudoku_matrix[inside_line][in_line]))
            inside_line += 1

        inside_line = 0

        numbers_to_be_checked.sort()
        if not len(list(set(numbers_to_be_checked) & set(SUBSET))) == 9:
            return False
        in_line += 1
    return True


def check_matrix_3_x_3(sudoku_matrix):
    in_line = inside_line = count = 0
    numbers_to_be_checked = []
    while count < 21:
        while in_line < 3:
            while inside_line < 3:
                numbers_to_be_checked.append(int(sudoku_matrix[in_line][inside_line]))
                inside_line += 1
            inside_line = 0
            in_line += 1

        numbers_to_be_checked.sort()
        if not len(list(set(numbers_to_be_checked) & set(SUBSET))) == 9:
            return False
        numbers_to_be_checked = []
        count += 1
        in_line = 0
    return True


if __name__ == '__main__':
    sudoku_input = """
           295743861
            431865927
            876192543
            387459216
            612387495
            549216738
            763524189
            928671354
            154938672
        """
    result = check_sudoku(sudoku_input)
    print("Yes") if result else print("No")

    sudoku_input = """
            195743862
            431865927
            876192543
            387459216
            612387495
            549216738
            763524189
            928671354
            254938671
        """
    result = check_sudoku(sudoku_input)
    print("Yes") if result else print("No")
