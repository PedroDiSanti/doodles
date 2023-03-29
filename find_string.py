# Find String
# The task is to write a program which answers the following question:
# are the characters comprising the first string hidden inside the second string?

def find_string(first_str: str, second_str: str) -> bool:
    index = 0

    string_to_be_found = first_str.lower()
    string_to_be_searched = second_str.lower()

    for char in string_to_be_found:
        index = string_to_be_searched.find(char, index)
        if index == -1:
            return False
    return True


if __name__ == '__main__':
    first_string = "donor"
    second_string = "Nabucodonosor"
    result = find_string(first_string, second_string)
    print("Yes") if result else print("No")

    first_string = "donut"
    second_string = "Nabucodonosor"
    result = find_string(first_string, second_string)
    print("Yes") if result else print("No")
