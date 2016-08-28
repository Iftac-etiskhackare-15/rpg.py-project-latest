class RNG:
    def __init__(self):
        # constructor
        _min = 0
        _max = 10
    def Get(self, arg1, arg2):
        min = arg1
        max = arg2
        return randint(min, max)