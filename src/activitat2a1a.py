from math import *

from mylib.arithmetic_mean import arithmeticMean
from mylib.class_patient import Patient
from mylib.class_patients import Patients
from mylib.euclidean import euclidean as deuclidea
from numpy import *
from types import *
from time import clock

# parametros
k = 4

# declaracion de funciones
def contar(l):
    p = {}
    for x in l:
        p.setdefault(x, 0)
        p[x] += 1
    return p

def classify(t):
    ds = list(map(deuclidea, train, [t for x in range(len(train))]))
    kcl = contar([sorted([(ds[i], clasesTrain[i]) for i in range(len(train))], key=lambda x: x[0])[i][1] for i in range(k)])
    return max([(x, kcl[x]) for x in kcl.keys()], key=lambda x: x[1])[0]

start = clock()
print ("Activitat: 2-knn (PAC2 / Activitat 1)")
print("")

#
# Obtenir pacients per l'entrenament i la prediccio
#
print ("Llegint dades del fitxer:")
lines = [(l.strip()).split(",") for l in (open("echocardiogram.csv").readlines())]
patients_train = Patients()
patients_prediction = Patients()
i = 0
for args in lines:
    patient = Patient(args)
    if ((i % 3) == 0):
        patients_prediction.Add(patient)
    else:
        patients_train.Add(patient)
    i += 1

numero_components = 7

print ("> Entrenament <")
print ("Nombre de pacients entrenament:", patients_train.Size())
patients_train.SetAutoFixedValues(arithmeticMean)
patients_train.SetAutoRang()
patients_train.Fix()
d_patients_train, class_patients_train = patients_train.ConvertToProcessData(numero_components)

print ("> Prediccio <")
print ("Nombre de pacients prediccio:", patients_prediction.Size())
patients_prediction.SetFixedValues(patients_train.GetFixedValues())
patients_prediction.SetRang(patients_train.GetRang())
patients_prediction.Fix()
d_patients_prediction, class_patients_prediction = patients_prediction.ConvertToProcessData(numero_components)
print("")

#
# Classificacio knn
#
print ("Classificacio:")
print ("Formatant dades per al classificador...")
train  = []
clasesTrain = []
for i in range(shape(d_patients_train)[0]):
    train.append(list(d_patients_train[i]))
    clasesTrain.append(class_patients_train[i][0])
test  = []
clasesTest = []
for i in range(shape(d_patients_prediction)[0]):
    test.append(list(d_patients_prediction[i]))
    clasesTest.append(class_patients_prediction[i][0])

# Entrenamiento
print ("Entrenament...")
clases = contar(clasesTrain)

# Clasificacion
predicciones = list(map(classify, test))

# Numero de correctos
print ("Prec.:", format(float(len(list(filter(lambda x: x[0] == x[1], zip(*[predicciones, clasesTest]))))) / float(len(test)) * 100.0, '.4f'), '%')
print("")

print ("Temps execucio:",format(clock() - start, '.4f'),"segons")