import math
class LONGINT:
    def __init__(self, value):
        if type(value) != type("hello"):
            raise TypeError("Hi, please wake up")
        if value[0] != "-":
            self._value = str(value)
            self._sign = 1
        else:
            self._value = str(-1 * value[1:])
            self._sign = 0
    def getValue(self):
        if self._sign:
            return self._value
        else:
            return "-" + self._value
    def setValue(self, value):
        if value > 0:
            self._value = str(value)
            self._sign = 1
        else:
            self._value = str(-1 * value)
            self._sign = 0
    def add(self, value):
        # value1 = self._value
        # value2 = value
        # value3 = ""
        # max_length = max(len(value1), len(value2))
        # for i in range(max_length, 0, -1):
        #     current= str(int(value1[-i]) + int(value2-i))
        self.setValue(str())
