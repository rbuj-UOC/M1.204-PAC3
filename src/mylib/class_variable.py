from mylib.class_rang import Rang

class Variable:
    # method's constructor
    def __init__(self):
        self.__fixedValue=0

    def SetRang(self, args):
        self.__rang = Rang(args)

    def GetRang(self):
        return self.__rang.GetRang()

    def SetFixedValue(self, arg):
        self.__fixedValue = arg

    def FixedValue(self):
        return self.__fixedValue

    def Normalize(self, valor):
        return self.__rang.Assign(valor)

