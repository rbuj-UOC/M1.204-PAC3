# survival -- the number of months patient survived (has survived, if patient is
# still alive).  Because all the patients had their heart attacks at different
# times, it is possible that some patients have survived less than one year but
# they are still alive.  Check the second variable to confirm this. Such patients
# cannot be used for the prediction task mentioned above.

class Survival:
    
    # method's constructor
    def __init__(self, value):
        if (value == '?'):
            self.__isNull = True
            self.SetValue(value)
        else:
            try:
                self.SetValue(float(value))
                self.__isNull = False
            except:
                self.__isNull = True

    def IsNull(self):
        return self.__isNull
    
    def GetValue(self):
        return self.__value
    
    def SetValue(self, value):
        self.__value = value
