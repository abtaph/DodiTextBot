
import time


class timeRep:
    def _init_(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes

    def __sub__(self, other):
        newHour = self.hour - other.hour
        newMinute = self.minutes - other.minutes
        return timeRep(newHour, newMinute)
