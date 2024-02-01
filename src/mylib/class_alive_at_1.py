# Boolean-valued. Derived from the first two attributes. 0 means patient was
# either dead after 1 year or had been followed for less than 1 year. 1 means
# patient was alive at 1 year.

class AliveAtOne:
    
    # method's constructor
    def __init__(self, value):
        if (value=='?'):
            self.SetValue(value)
            self.__isNull=True
        else:
            self.SetValue(value=='1')
            self.__isNull=False
    def IsNull(self):
        return self.__isNull
    def GetValue(self):
        return self.__value
    def SetValue(self, value):
        self.__value = value
