import random


def generate_mega_sena(quantity_of_numbers_to_generate=6, list_of_numbers=None):
    """Generates a specified quantity of unique random numbers ranging from 1 to 60. 

    Args:
        quantity_of_numbers_to_generate (int): Quantity of unique random numbers to generate. Default is 6.
        list_of_numbers (list): List to append the generated numbers to. If not specified,
                                a new list will be created.

    Returns:
        list_of_numbers (list): List containing the generated unique random numbers.
    """
    if list_of_numbers is None:
        list_of_numbers = []

    while len(list_of_numbers) < quantity_of_numbers_to_generate:
        number_to_add = random.randint(1, 60)
        if number_to_add not in list_of_numbers:
            list_of_numbers.append(number_to_add)

    list_of_numbers.sort()
    return list_of_numbers


if __name__ == '__main__':
    quantity_of_games = 2
    for _ in range(quantity_of_games):
        numbers = generate_mega_sena(quantity_of_numbers_to_generate=6, list_of_numbers=[])
        print(numbers)
