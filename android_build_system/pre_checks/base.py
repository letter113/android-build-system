class BaseCheck:
    def __init__(self, message):
        self.message = message

    def _check(self):
        raise NotImplemented

    def check(self):
        if self._check():
            print(self.message + "\t[OK]")
            return True
        print(self.message + "\t[NO]")