from datetime import datetime
import re


def get_days_from_today(date: str) -> int:
    if re.match(r"^\d{1,4}-\d{1,2}-\d{1,2}$", date) is None:
        return "Невірний формат дати. Спробуйте 'РРРР-ММ-ДД'"
    
    return (datetime.today().date() - datetime.strptime(date, "%Y-%m-%d").date()).days

date_string = "2021-10-09"
date_string_2 = "2025-03-30"
date_string_3 = "2026-10-09"

print(get_days_from_today(date_string))
print(get_days_from_today(date_string_2))
print(get_days_from_today(date_string_3))

