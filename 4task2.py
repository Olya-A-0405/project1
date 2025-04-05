from pathlib import Path

def get_cats_info(path):
    cats_list = []  
    
    try:
        with open(path, "r") as file:
            for line in file:
                data = line.strip().split(",") 
                
                if len(data) == 3:  
                    cat_id, name, age = data
                    cats_list.append({"id": cat_id, "name": name, "age": age})  

        return cats_list  

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

path_to_file = "4task2.txt"  
cats_info = get_cats_info(path_to_file)

print(*cats_info, sep = '\n')