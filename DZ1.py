from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()  
        today_date = datetime.today().date()  
        delta = today_date - given_date  
        return delta.days 
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

print(get_days_from_today("2021-10-09"))  
print(get_days_from_today("2026-02-15"))  
print(get_days_from_today("not a date"))  

