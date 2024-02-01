# still-alive -- a binary variable.  0=dead at end of survival period, 1 means
# still alive 
                     
class StillAlive:
    
    # method's constructor
    def __init__(self, value):
        if (value == '?'):
            self.__isNull = True
            self.SetValue(value)
        else:
            self.SetValue(value == '1')
            self.__isNull = False

    def IsNull(self):
        return self.__isNull
    
    def GetValue(self):
        return self.__value
    
    def SetValue(self, value):
        self.__value = value
