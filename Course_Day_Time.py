import os

class Time:
    def __init__(self, day, period_begin, period_end):
        self.day = day
        self.period_begin = period_begin
        self.period_end = period_end
        
    def getTime(self):
        print(self.day)
        print(self.period_begin)
        print(self.period_end)
        