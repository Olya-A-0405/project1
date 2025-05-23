import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or quantity > (max - min + 1):
        return []
    
    return sorted(random.sample(range(min, max + 1), quantity))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
