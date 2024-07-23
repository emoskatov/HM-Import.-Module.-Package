from application.db.people import *
from application.salary import *
from datetime import datetime

if __name__ == "__main__":
    print(f'Сегодня: {datetime.today().strftime("%d-%m-%y")} ')
    get_employees()
    calculate_salary()