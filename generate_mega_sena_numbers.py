import random


def generate_mega_sena(quantity_of_numbers_to_generate=6, list_of_numbers=[]):
    try:
        for quantity in range(quantity_of_numbers_to_generate):
            number_to_add = random.randint(1, 60)
            if number_to_add in list_of_numbers:
                number_to_add = generate_mega_sena(1)[0]
            list_of_numbers.append(number_to_add)
        list_of_numbers.sort()
        return list_of_numbers
    except Exception as error:
        print(f"ERROR: {error}")


if __name__ == '__main__':
    quantity_of_games = 5
    while quantity_of_games > 0:
        numbers = generate_mega_sena(quantity_of_numbers_to_generate=6, list_of_numbers=[])
        print(numbers)
        quantity_of_games -= 1
