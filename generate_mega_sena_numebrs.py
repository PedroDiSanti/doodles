import random

list_of_numbers = []

def generate_mega_sena(quantity_of_numbers):
    for i in range(quantity_of_numbers):
        number_to_add = random.randint(1, 60) 
        if number_to_add not in list_of_numbers:
            list_of_numbers.append(number_to_add)
        else:
            number_to_add = generate_mega_sena(1)
            list_of_numbers.append(number_to_add)
    list_of_numbers.sort()
    return list_of_numbers

if __name__ == '__main__':
    numbers = generate_mega_sena(6)
    print(numbers)
    
    
