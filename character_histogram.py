# Asks the user for the input;
# Reads the file (if possible) and counts all the Latin letters (lower-and upper-case letters are treated as equal);
# Prints a simple histogram in alphabetical order (only non-zero counts should be presented);

from os import strerror

TXT = './utils/new_file.txt'


def write_file():
    with open(TXT, 'w', encoding='utf-8') as f:
        f.write(input('Your message: '))


def count_characters():
    dict_of_letter = {}

    text = read_file()
    for letter in text:
        total = dict_of_letter.get(letter.lower(), 0)
        total += 1
        dict_of_letter.update({letter.lower(): total})
    return dict_of_letter


def read_file():
    try:
        file = open(TXT, "r")
        file_text = file.read()
        file.close()
    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))

    return file_text


if __name__ == '__main__':
    write_file()

    histogram = count_characters()
    for key, value in histogram.items():
        print(f'{key}->{value}')
