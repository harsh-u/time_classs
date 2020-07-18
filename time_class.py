class Time:
    def __init__(self, hour, min):
        self.hour = hour
        self.min = min

    def displayTime(self):
        return f'The Time is {self.hour} hr {self.min} min'

    def displayMinute(self):
        minute = (self.hour * 60) + self.min
        return f'time in minute is {minute}'

    # def addTime(self, t1, t2):


t1 = Time(1,20)
t2 = Time(2,40)
print(t1.displayMinute())
print(t2.displayTime())


