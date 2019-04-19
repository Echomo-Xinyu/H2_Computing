# implement a class @BaseKInt
class BaseKInt():
    def __init__(self, value, base):
        self.mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.value = value
        self.base = base
        self.representation = self.getBaseK(value, base)
    def getBaseK(self, value, base):
        result = ""
        mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while value > 0:
            digit = mapping[value % base]
            result = digit + result
            value =  value// base
        return result
    def add(self, another_BaseKInt, new_base):
        result = self.value + another_BaseKInt.value
        return BaseKInt(result, new_base)
    def multiply(self, another_BaseKInt, new_base):
        result = self.value * another_BaseKInt.value
        return BaseKInt(result, new_base)
    def modulo(self, another_BaseKInt, new_base):
        result = self.value % another_BaseKInt.value
        return BaseKInt(result, new_base)
    def quotient(self, another_BaseKInt, new_base):
        result = self.value // another_BaseKInt.value
        return BaseKInt(result, new_base)
    def exponent(self, another_BaseKInt, new_base):
        result = self.value ** another_BaseKInt.value
        return BaseKInt(result, new_base)
    def factorial(self, new_base):
        result = 1
        for i in range(2, self.value+1):
            result *= i
        return BaseKInt(result, new_base)
