from application.db.people import get_employees as gt
from application.salary import calculate_salary as cs
from datetime import datetime

if __name__ == "__main__":
    print(f'Сегодня: {datetime.today().strftime("%d-%m-%y")} ')
    gt()
    cs()