
class task:
    def __init__(self, description, finishTime):
        self.description = description
        self.finishTime = finishTime

    def __sub__(self, other):
        return task(self.description, self.finishTime - other.finishTime)
