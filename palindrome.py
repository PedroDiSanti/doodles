# Check Palindrome
# asks the user for some text;
# checks whether the entered text is a palindrome, and prints result.

def check_palindrome(original_str: str) -> bool:
    original_str = original_str.replace(" ", "").lower()
    reversed_str = original_str[::-1]

    if original_str == reversed_str:
        return True
    return False


if __name__ == '__main__':
    cipher_to_check = "Ten animals I slam in a net"
    result = check_palindrome(cipher_to_check)
    print("It's a palindrome") if result else print("It's not a palindrome")
