
import time


class timeRep:
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes

    def __sub__(self, other):
        newHour = self.hour - other.hour
        newMinute = self.minutes - other.minutes
        return timeRep(newHour, newMinute)

    def __add__(self, other):
        newHour = self.hour + other.hour
        newMinute = self.minutes - other.minutes
        return timeRep(newHour, newMinute)

    def __str__(self):
        return str(self.hour) + ":" + str(self.minutes)
