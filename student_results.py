# Write a program which:
# Asks the user for file name;
# Reads the file contents and counts the sum of the received points for each student;
# Prints a simple sorted report;

TAB = '\t'
TXT_PATH = './utils/'


def calculate_students_grades(file_to_order):
    dict_of_student_info = {}
    for data in file_to_order:
        list_of_data = data.split('\t')
        student_full_name = f'{list_of_data[0]} {list_of_data[1]}'
        student_total_grade = dict_of_student_info.get(student_full_name, 0.0) + float(list_of_data[2])
        dict_of_student_info.update({student_full_name: student_total_grade})
    return sorted(dict_of_student_info.items(), key=lambda x: x[0].lower())


def read_file(filename):
    try:
        with open(TXT_PATH + filename + ".txt", 'r', encoding='UTF-8') as file:
            return file.read().splitlines()
    except FileNotFoundError as file_not_found:
        raise FileNotFoundError(file_not_found)
    return document


if __name__ == '__main__':
    filename_imputed = input('Select the file: ')
    students_grades = read_file(filename_imputed)
    ordered_student_grades = calculate_students_grades(students_grades)
    for student_grade in ordered_student_grades:
        print(f"{student_grade[0]}{TAB}{TAB}{TAB}{student_grade[1]}")
