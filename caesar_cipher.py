# Caesar cipher shifts
# asks the user for one line of text to encrypt;
# asks the user for a shift value (an integer number from the range 1..25
# note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
# prints out the encoded text.

def make_caesar_cipher(cipher_input: str, crypt_range: int) -> str:
    if crypt_range < 1 or crypt_range > 25:
        print("Error! Range should be between 1 and 25.")
        return

    cipher = ''
    for char in cipher_input:
        if not char.isalpha():
            cipher += char
            continue

        is_upper_case = True if char.isupper() else False
        code = create_cipher(char, crypt_range, is_upper_case)
        cipher += chr(code)
    return cipher


def create_cipher(char: str, crypt_range: int, is_upper: bool) -> str:
    code = ord(char) + crypt_range
    if is_upper:
        char = char.upper()
        if code > ord('Z'):
            code = (code - ord('Z') - 1) + ord('A')
    else:
        char = char.lower()
        if code > ord('z'):
            code = (code - ord('z') - 1) + ord('a')
    return code


if __name__ == '__main__':
    cipher_to_encrypt = "abcxyzABCxyz 123"
    cipher_encrypted = "cdezabCDEzab 123"
    cipher_encrypted_range = 2
    result = make_caesar_cipher(cipher_to_encrypt, cipher_encrypted_range)

    try:
        assert result == cipher_encrypted
    except AssertionError as error:
        print(error)
