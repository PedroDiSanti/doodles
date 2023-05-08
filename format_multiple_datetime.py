import datetime

if __name__ == '__main__':
    created_datetime = datetime.datetime(day=4, month=11, year=2020, hour=14, minute=53, second=00)
    print(created_datetime.strftime('%Y/%m/%d %H:%M:%S'))
    print(created_datetime.strftime('%Y/%B/%d %H:%M:%S %p'))
    print(created_datetime.strftime('%a, %Y %b %d'))
    print(created_datetime.strftime('%A, %Y %B %d'))
    print(created_datetime.strftime(f'Weekday: %w'))
    print(created_datetime.strftime(f'Day of the year: %j'))
    print(created_datetime.strftime(f'Week number of the year: %W'))
