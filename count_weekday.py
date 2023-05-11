# Create a class called MyCalendar that extends the Calendar class;
# Create the count_weekday_in_year method with the year and weekday parameters.
# The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday.
# The method should return the number of days as an integer;
# The implementation, use the monthdays2calendar method of the Calendar class.

from calendar import Calendar


class MyCalendar(Calendar):
    def __init__(self):
        self.calendar = Calendar()

    def count_weekday_in_year(self, year, weekday):
        total_of_weekday = 0
        for month in range(1, 13):
            month_matrix = self.calendar.monthdays2calendar(year=year, month=month)

            week = 0
            while week < len(month_matrix):
                for (x, y) in month_matrix[week]:
                    if y == weekday and x != 0:
                        total_of_weekday += 1
                week += 1

        return total_of_weekday


if __name__ == '__main__':
    calendar = MyCalendar()

    result = calendar.count_weekday_in_year(year=2019, weekday=0)
    print(result)

    result = calendar.count_weekday_in_year(year=2000, weekday=6)
    print(result)
