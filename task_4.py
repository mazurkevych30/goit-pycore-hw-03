from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)

        if birthday_this_year > today:
            if (birthday_this_year-today).days <= 7:
                match birthday_this_year.weekday():
                    case 5:
                        birthday_this_year += timedelta(days=2)
                    case 6:
                        birthday_this_year += timedelta(days=1)

                upcoming_birthdays.append({"name": user["name"], "congratulation_date": datetime.strftime(birthday_this_year, "%Y.%m.%d")})
    
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.12.14"},
    {"name": "Jane Smith", "birthday": "1990.12.10"},
    {"name": "Jane Smith", "birthday": "1990.12.17"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
