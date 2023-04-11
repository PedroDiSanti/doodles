# Weeker
# Your task is to implement a class that will be able to store and to manipulate the days of the week;
# Objects of the class should be "printable";
# The class should be equipped with one-parameter methods called add_days(n) and subtract_days(n),
# with n being an integer number and updating the day of week stored inside the object in the way
# reflecting the change of date by the indicated number of days, forward or backward.

class WeekDayError(Exception):
    pass


class Weeker:
    def __init__(self, day):
        self.days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        if day in self.days_of_week:
            self.day = day
        else:
            raise WeekDayError

    def __str__(self):
        return self.day

    def add_days(self, n):
        total_to_add = n % 7
        index_of_current_day = self.days_of_week.index(self.day)
        self.day = self.days_of_week[index_of_current_day + total_to_add]

    def subtract_days(self, n):
        total_to_add = n % 7
        index_of_current_day = self.days_of_week.index(self.day)
        self.day = self.days_of_week[index_of_current_day - total_to_add]


if __name__ == '__main__':
    try:
        weekday = Weeker('Mon')
        print(weekday)
        weekday.add_days(15)
        print(weekday)
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker('Monday')
    except WeekDayError:
        print("Sorry, I can't serve your request.")
