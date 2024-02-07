from datetime import datetime, timedelta
from calendar import isleap, leapdays


def _str_date_to_datetime(date: str) -> datetime:
    dt_args = tuple(map(lambda val: int(val), date.split(' ')))
    return datetime(*dt_args, tzinfo=None)


def _count_days(start_dt: datetime, end_dt: datetime) -> int:
    delta = end_dt - start_dt
    if start_dt.year != end_dt.year:
        leap_days = leapdays(start_dt.year, end_dt.year)
        return delta.days - leap_days
    else:
        if isleap(start_dt.year) and \
           start_dt < datetime(start_dt.year, 3, 1) and \
           end_dt > datetime(end_dt.year, 2, 29):
               return delta.days - 1
        else:
            return delta.days


def main(input: str) -> str:
    start_date, end_date = input.split('\n')
    start_dt, end_dt = _str_date_to_datetime(start_date), \
                       _str_date_to_datetime(end_date)
    days = _count_days(start_dt, end_dt)
    seconds = (end_dt - start_dt - timedelta(days=days)).seconds
    return f"{days} {seconds}"


def test1():
    result = main("980 2 12 10 30 1\n"
                  "980 3 1 10 31 37")
    assert result == '17 96', \
        'Тест 1 не пройден!'
    return 'Тест 1 пройден!'


def test2():
    assert main('1001 5 20 14 15 16',
                '9009 9 11 12 21 11') == '2923033 79555', \
        'Тест 2 не пройден!'
    return 'Тест 2 пройден!'


if __name__ == '__main__':
    try:
        print(test1())
        print(test2())
    except AssertionError as err:
        print(err)
    else:
        print('Все тесты успешно пройдены!')
