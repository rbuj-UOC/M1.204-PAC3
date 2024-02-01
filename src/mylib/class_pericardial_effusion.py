# pericardial-effusion -- binary. Pericardial effusion is fluid around the heart.
# 0=no fluid, 1=fluid

class PericardialEffusion:
    
    # method's constructor
    def __init__(self, value):
        if (value == '?'):
            self.__isNull = True
            self.SetValue(value)
        else:
            self.SetValue(float(value))
            self.__isNull = False

    def IsNull(self):
        return self.__isNull
    
    def GetValue(self):
        return self.__value
    
    def SetValue(self, value):
        self.__value = value
