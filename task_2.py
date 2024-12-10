import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int] | str:
    if min < 1 or max > 1000:
        return "Мінімальне значення повинно бути більши 0, а максимальне менше 1000."
    elif min > max or max-min < quantity:
        return f"Мінімальне значення більше максимального. Або недостатній діапазон чисел для списку з {quantity} унікальних чисел."

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min,max))
    
    numbers = list(numbers)
    numbers.sort()
    return numbers


print(get_numbers_ticket(10, 11, 6))