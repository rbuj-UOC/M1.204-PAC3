class Rang:
    # method's constructor
    def __init__(self, args):
        self.__maxim = args[0]
        self.__minim = args[1]

    def __init__(self, args):
        self.__maxim = args[0]
        self.__minim = args[1]

    def Maxim(self):
        return self.__maxim

    def Minim(self):
        return self.__minim

    def Assign(self, valor):
        return (valor - self.__minim) / (self.__maxim - self.__minim)

    def GetRang(self):
        return self.Maxim(), self.Minim()
