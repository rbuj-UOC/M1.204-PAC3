from mylib.class_variable import Variable
from mylib.pca import *
from mylib.ranging import *
from numpy import *

class Patients:
    
    # method's constructor
    def __init__(self):
        self.__patients = []
        self.__survival = Variable()
        self.__ageAtHeartAttack = Variable()
        self.__fractionalShortening = Variable()
        self.__epss = Variable()
        self.__lvdd = Variable()
        self.__wallMotionIndex = Variable()
        self.__pericardialEffusion = Variable()

    # add a patient
    def Add(self, patient):
        self.__patients.append(patient)

    # return the patients's number
    def Size(self):
        return len(self.__patients)

    # fix missing values and ranging values
    def Fix(self):
        print ("Nombre de variables booleans inicialment no assignades:", self.NumMissing_Boolean())
        print ("Nombre de variables numeriques inicialment no assignades:", self.NumMissing_Numeric())
        # corregir els valors numerics que falten
        self.__FixMissing()
        # ranging
        self.__Ranging()

    # set values for missing values of variables
    def SetFixedValues(self, args):
        self.__survival.SetFixedValue(args[0])
        self.__ageAtHeartAttack.SetFixedValue(args[1])
        self.__fractionalShortening.SetFixedValue(args[2])
        self.__epss.SetFixedValue(args[3])
        self.__lvdd.SetFixedValue(args[4])
        self.__wallMotionIndex.SetFixedValue(args[5])
        self.__pericardialEffusion.SetFixedValue(args[6])

    # set values for missing values of variables
    def SetAutoFixedValues(self, funcFixedValue):
        self.__survival.SetFixedValue(funcFixedValue(self.__ListNotNull_Survival()))
        self.__ageAtHeartAttack.SetFixedValue(funcFixedValue(self.__ListNotNull_AgeAtHeartAttack()))
        self.__fractionalShortening.SetFixedValue(funcFixedValue(self.__ListNotNull_FractionalShortening()))
        self.__epss.SetFixedValue(funcFixedValue(self.__ListNotNull_Epps()))
        self.__lvdd.SetFixedValue(funcFixedValue(self.__ListNotNull_Lvdd()))
        self.__wallMotionIndex.SetFixedValue(funcFixedValue(self.__ListNotNull_WallMotionIndex()))
        self.__pericardialEffusion.SetFixedValue(funcFixedValue(self.__ListNotNull_PericardialEffusion()))

    # get values for missing values of variables
    def GetFixedValues(self):
        return self.__survival.FixedValue(), self.__ageAtHeartAttack.FixedValue(), self.__fractionalShortening.FixedValue(), self.__epss.FixedValue(), self.__lvdd.FixedValue(), self.__wallMotionIndex.FixedValue(), self.__pericardialEffusion.FixedValue()

    # set rang from local values
    def SetAutoRang(self):
        # pericardial-effusion ja esta dins del rang [0,1]
        self.__survival.SetRang(limitValues(self.__ListNotNull_Survival()))
        self.__ageAtHeartAttack.SetRang(limitValues(self.__ListNotNull_AgeAtHeartAttack()))
        self.__fractionalShortening.SetRang(limitValues(self.__ListNotNull_FractionalShortening()))
        self.__epss.SetRang(limitValues(self.__ListNotNull_Epps()))
        self.__lvdd.SetRang(limitValues(self.__ListNotNull_Lvdd()))
        self.__wallMotionIndex.SetRang(limitValues(self.__ListNotNull_WallMotionIndex()))

    # set rang of variables
    def SetRang(self, args):
        # pericardial-effusion ja esta dins del rang [0,1]
        self.__survival.SetRang(args[0])
        self.__ageAtHeartAttack.SetRang(args[1])
        self.__fractionalShortening.SetRang(args[2])
        self.__epss.SetRang(args[3])
        self.__lvdd.SetRang(args[4])
        self.__wallMotionIndex.SetRang(args[5])

    # get rang of variables
    def GetRang(self):
        # pericardial-effusion ja esta dins del rang [0,1]
        return self.__survival.GetRang(), self.__ageAtHeartAttack.GetRang(), self.__fractionalShortening.GetRang(), self.__epss.GetRang(), self.__lvdd.GetRang(), self.__wallMotionIndex.GetRang()

    def __ListNotNull_Survival(self):
        aList = []
        for patient in self.__patients:
            if patient.hasValue_Survival():
                aList.append(patient.get_Survival())
        return aList
    def __ListNotNull_AgeAtHeartAttack(self):
        aList = []
        for patient in self.__patients:
            if patient.hasValue_AgeAtHeartAttack():
                aList.append(patient.get_AgeAtHeartAttack())
        return aList
    def __ListNotNull_FractionalShortening(self):
        aList = []
        for patient in self.__patients:
            if patient.hasValue_FractionalShortening():
                aList.append(patient.get_FractionalShortening())
        return aList
    def __ListNotNull_Epps(self):
        aList = []
        for patient in self.__patients:
            if patient.hasValue_Epss():
                aList.append(patient.get_Epss())
        return aList
    def __ListNotNull_Lvdd(self):
        aList = []
        for patient in self.__patients:
            if patient.hasValue_Lvdd():
                aList.append(patient.get_Lvdd())
        return aList
    def __ListNotNull_WallMotionIndex(self):
        aList = []
        for patient in self.__patients:
            if patient.hasValue_WallMotionIndex():
                aList.append(patient.get_WallMotionIndex())
        return aList
    def __ListNotNull_PericardialEffusion(self):
        aList = []
        for patient in self.__patients:
            if patient.hasValue_PericardialEffusion():
                aList.append(patient.get_PericardialEffusion())
        return aList

    # fix the missing values
    def __FixMissing(self):
        print ("Tractant variables numeriques sense assignar...")
        for idx in range(len(self.__patients)):
            if (not self.__patients[idx].hasValue_Survival()):
                self.__patients[idx].set_Survival(self.__survival.FixedValue())
            if (not self.__patients[idx].hasValue_AgeAtHeartAttack()):
                self.__patients[idx].set_AgeAtHeartAttack(self.__ageAtHeartAttack.FixedValue())
            if (not self.__patients[idx].hasValue_FractionalShortening()):
                self.__patients[idx].set_FractionalShortening(self.__fractionalShortening.FixedValue())
            if (not self.__patients[idx].hasValue_Epss()):
                self.__patients[idx].set_Epss(self.__epss.FixedValue())
            if (not self.__patients[idx].hasValue_Lvdd()):
                self.__patients[idx].set_Lvdd(self.__lvdd.FixedValue())
            if (not self.__patients[idx].hasValue_WallMotionIndex()):
                self.__patients[idx].set_WallMotionIndex(self.__wallMotionIndex.FixedValue())
            if (not self.__patients[idx].hasValue_PericardialEffusion()):
                self.__patients[idx].set_PericardialEffusion(self.__pericardialEffusion.FixedValue())

    # ranging
    def __Ranging(self):
        print ("Tractant valor de les variables: ranging...")
        for idx in range(len(self.__patients)):
            self.__patients[idx].set_Survival(self.__survival.Normalize(self.__patients[idx].get_Survival()))
            self.__patients[idx].set_AgeAtHeartAttack(self.__ageAtHeartAttack.Normalize(self.__patients[idx].get_AgeAtHeartAttack()))
            self.__patients[idx].set_FractionalShortening(self.__fractionalShortening.Normalize(self.__patients[idx].get_FractionalShortening()))
            self.__patients[idx].set_Epss(self.__epss.Normalize(self.__patients[idx].get_Epss()))
            self.__patients[idx].set_Lvdd(self.__lvdd.Normalize(self.__patients[idx].get_Lvdd()))
            self.__patients[idx].set_WallMotionIndex(self.__wallMotionIndex.Normalize(self.__patients[idx].get_WallMotionIndex()))

    # return total of missing assignaments of boolean variables
    def NumMissing_Boolean(self):
        total = 0
        for patient in self.__patients:
            total += patient.getMissing_Boolean()
        return total

    # return total of missing assignaments of numeric variables
    def NumMissing_Numeric(self):
        total = 0
        for patient in self.__patients:
            total += patient.getMissing_Numeric()
        return total

    # to matrix
    def ConvertToProcessData(self, num):
        myData  = zeros([self.Size(), num], float)
        myClass = zeros([self.Size(), 1], int)
        for idx in range(len(self.__patients)):
            if (num >= 1):
                myData[idx][0] = self.__patients[idx].get_Survival()
            if (num >= 2):
                myData[idx][1] = self.__patients[idx].get_AgeAtHeartAttack()
            if (num >= 3):
                myData[idx][2] = self.__patients[idx].get_WallMotionIndex()
            if (num >= 4):
                myData[idx][3] = self.__patients[idx].get_FractionalShortening()
            if (num >= 5):
                myData[idx][4] = self.__patients[idx].get_Epss()
            if (num >= 6):
                myData[idx][5] = self.__patients[idx].get_Lvdd()
            if (num == 7):
                myData[idx][6] = self.__patients[idx].get_PericardialEffusion()
            myClass[idx] = self.__patients[idx].get_StillAlive()
        return myData, myClass

    # get the variable's name
    def GetVariablesNameProcessData(self, indexs):
        variables_name  = ["Survival", "AgeAtHeartAttack", "WallMotionIndex", "FractionalShortening", "Epss", "Lvdd", "PericardialEffusion"]
        answer = []
        for i in range(len(indexs)):
            answer.append(variables_name[indexs[i]])
        return answer

    def GetPCA(self, num_variables, percentatge):
        d, myClass = self.ConvertToProcessData(num_variables)
        PCA_indexs_components, PCA_VEPS_Orcre_DEC = GetPCA(d, percentatge)
        print ("Components:",self.GetVariablesNameProcessData(PCA_indexs_components))
        return PCA_VEPS_Orcre_DEC, size(PCA_indexs_components)

    # get the variable's name
    def ConvertToProcessDataPCA(self, tipus, numero_components, PCA_VEPS_Orcre_DEC, PCA_numero_components):
        d, myClass = self.ConvertToProcessData(numero_components)
        print ("PCA: Projectant dades",tipus,"amb els",PCA_numero_components,"VEPS amb mes VAP...")
        d_PCA = ProyectPCA(d, PCA_VEPS_Orcre_DEC, PCA_numero_components)
        return d_PCA, myClass

    def Show(self):
        for patient in self.__patients:
            patient.Show()
