class Lazy:
    enabled=False
    def __init__(self, _enabled):
        self.enabled = _enabled

    def cls(self):
        if self.enabled == True:
            _clear = "\n" * 100
            print _clear
        return 0

    def line(self):
        if self.enabled == True:
            _clear = "\n"
            print _clear
        return 0
