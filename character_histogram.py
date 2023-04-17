# Asks the user for the input;
# Reads the file (if possible) and counts all the Latin letters (lower-and upper-case letters are treated as equal);
# Prints a simple histogram in alphabetical order (only non-zero counts should be presented);
# The output histogram will be sorted based on the characters' frequency;
# The histogram should be sent to a file with the same name as the input one, but with the suffix '.hist';

from os import strerror

TXT = './utils/new_file.txt'
HIST = './utils/new_file.hist'


def write_text_file():
    with open(TXT, 'w', encoding='utf-8') as f:
        f.write(input('Your message: '))


def count_characters():
    dict_of_letter = {}

    text = read_file()
    for letter in text:
        total = dict_of_letter.get(letter.lower(), 0)
        total += 1
        dict_of_letter.update({letter.lower(): total})

    return sorted(dict_of_letter.items(), reverse=True, key=lambda item: item[1])


def read_file():
    try:
        file = open(TXT, "r")
        file_text = file.read()
        file.close()
    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))

    return file_text


def write_hist_file(stream_to_write):
    with open(HIST, 'w', encoding='utf-8') as f:
        for histogram_item in histogram:
            string_to_save = f'{histogram_item[0]}->{histogram_item[1]}'
            print(string_to_save)
            f.write(f'{string_to_save}\n')
    f.close()


if __name__ == '__main__':
    write_text_file()
    histogram = count_characters()
    write_hist_file(histogram)
