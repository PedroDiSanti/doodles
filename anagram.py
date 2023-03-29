# Check Anagram
# asks the user for two separate texts;
# checks whether, the entered texts are anagrams and prints the result.

def check_anagram(first_str: str, second_str: str) -> bool:
    dict_for_first_str = create_dict_by_letter(first_str.lower())
    dict_for_second_str = create_dict_by_letter(second_str.lower())
    return True if dict_for_first_str == dict_for_second_str else False


def create_dict_by_letter(str_to_create_dict: str) -> dict:
    dict_for_str = {}
    for char in str_to_create_dict:
        if char not in dict_for_str:
            dict_for_str[char] = 1
        else:
            dict_for_str[char] = +1
    return dict_for_str


if __name__ == '__main__':
    str_1 = "Listen"
    str_2 = "Silent"
    result = check_anagram(str_1, str_2)
    print("Anagrams") if result else print("Not anagrams")

    str_1 = "modern"
    str_2 = "norman"
    result = check_anagram(str_1, str_2)
    print("Anagrams") if result else print("Not anagrams")
