import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    numbers = re.findall(r' \d+\.\d+ ', text)
    for number in numbers:
        yield float(number.strip())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 i 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
