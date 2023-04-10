# Scenario
# We need a class able to count seconds.

# Objects of the class should be "printable"
# Convert themselves into strings of the following form: "hh:mm:ss",
# With leading zeros added when any of the values is less than 10;
# The class should be equipped with parameterless methods called next_second() and previous_second()
# Incrementing the time stored inside objects by +1/-1 second respectively.


number_to_add_0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


class Timer:
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f'{self.hour}:{self.minute}:{self.second}'

    def set_time_to_str(self, hour, minute, second):
        if hour in number_to_add_0:
            self.hour = "0" + str(hour)
        else:
            self.hour = str(hour)

        if minute in number_to_add_0:
            self.minute = "0" + str(minute)
        else:
            self.minute = str(minute)

        if second in number_to_add_0:
            self.second = "0" + str(second)
        else:
            self.second = str(second)

    @staticmethod
    def set_time_to_int(hour, minute, second):
        return int(hour), int(minute), int(second)

    def next_second(self):
        hour, minute, second = self.set_time_to_int(self.hour, self.minute, self.second)

        second += 1
        if second >= 60:
            second = 0
            minute += 1
        if minute >= 60:
            minute = 0
            hour += 1
        if hour >= 24:
            hour = 0
        self.set_time_to_str(hour, minute, second)

    def prev_second(self):
        hour, minute, second = self.set_time_to_int(self.hour, self.minute, self.second)

        second -= 1
        if second < 0:
            second = 59
            minute -= 1
        if minute < 0:
            minute = 59
            hour -= 1
        if hour < 0:
            hour = 23
        self.set_time_to_str(hour, minute, second)


if __name__ == '__main__':
    timer = Timer(23, 59, 59)
    print(timer)
    timer.next_second()
    print(timer)
    timer.prev_second()
    print(timer)
    timer.next_second()
    print(timer)
    timer.next_second()
    print(timer)
