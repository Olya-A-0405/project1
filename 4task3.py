import sys
import os
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def visualize_directory_structure(directory, indent=0):
    """Функція для рекурсивного обходу директорії та виводу структури з кольорами."""
    try:
        path = Path(directory)
        
        if not path.exists():
            print(Fore.RED + "Помилка: Вказана директорія не існує.")
            return
        if not path.is_dir():
            print(Fore.RED + "Помилка: Вказаний шлях не є директорією.")
            return

        for item in sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())):
            if item.is_dir():
                print(" " * indent + Fore.BLUE + f"📂 {item.name}")
                visualize_directory_structure(item, indent + 4)  
            else:
                print(" " * indent + Fore.GREEN + f"📜 {item.name}")
    
    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python hw03.py>")
        sys.exit(1)

    directory_path = sys.argv[1]
    visualize_directory_structure(directory_path)
