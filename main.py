from application.db.people import get_employees as gt
from application.salary import calculate_salary as cs
from datetime import datetime
from pprint import pprint

if __name__ == "__main__":
    print(f'Сегодня: {datetime.today().strftime("%d-%m-%y")} ')
    gt()
    cs()
    pprint({1: "вывод", 2: "этого", 3: "сообщения", 4: "был", 5: "отформатирован", 6: "pprint"})
