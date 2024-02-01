# wall-motion-index -- equals wall-motion-score divided by number of segments
# seen.  Usually 12-13 segments are seen in an echocardiogram. Use this variable
# INSTEAD of the wall motion score.

class WallMotionIndex:
    
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
