# from datetime import date
from datetime import datetime,date
import random


def rand_day_not_xmas(start_date_ordinal, end_date_ordinal):
    random_day = date.fromordinal(random.randint(start_date_ordinal, end_date_ordinal))
    if random_day == "2021-12-25":
        print("POW")
        rand_day_not_xmas(start_date_ordinal, end_date_ordinal)
    else:
        return random_day


def run_script(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'I like big, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # start_date = date.today().replace(day=1, month=1).toordinal()
    # end_date = date.today().toordinal()
    # random_day = date.fromordinal(random.randint(start_date, end_date))
    # print(random_day)
    this_day = date.today()
    this_year = this_day.year
    start_date_ordinal = this_day.toordinal()

    print(f'start_date is... {start_date_ordinal}')
    end_date_ordinal = datetime.strptime(f'{this_year}-12-31', "%Y-%m-%d").toordinal()
    i = 0
    for i in range(1000000000):
        random_day = rand_day_not_xmas(start_date_ordinal, end_date_ordinal)
        print("out: ", random_day)
    # start_date_ordinal = datetime.strptime("")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_script('tiddies')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
