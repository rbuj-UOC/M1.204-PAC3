from mylib.arithmetic_mean import arithmeticMean
from mylib.class_patient import Patient
from mylib.class_patients import Patients
from mylib.euclidean import euclidean as deuclidea
from functools import reduce
from numpy import *
from types import *
from math import *
from time import clock

# declaracion de funciones
def contar(l):
    p = {}
    for x in l:
        p.setdefault(x, 0)
        p[x] += 1
    return p

def classify(t):
    ds = list(map(deuclidea, centroides, [t for x in range(len(centroides))]))
    return min([(ds[i], centroides[i][0]) for i in range(len(centroides))], key=lambda x: x[0].all())[1]

def calcularCentroides(classe):
    filt = list(filter(lambda x: x[0] == x[1], [(clasesTrain[i], classe, train[i]) for i in range(len(train))]))
    transp = list(zip(*[filt[i][2] for i in range(len(filt))]))
    return (classe, list(map(lambda l: reduce(lambda a, b: a + b, l) / clases[classe], transp)))

start = clock()
print ("Activitat: 2-lineal (PAC2 / Activitat 2)")
print ("")

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
# PCA: trobar quines variables proporcionen un 95% de varianca amb els  pacients
#      d'entrenament
#
print ("Analisi PCA:")
numero_components = 7
PCA_VEPS_Orcre_DEC, PCA_numero_components = patients_train.GetPCA(numero_components, 0.95)
d_patients_train, class_patients_train = patients_train.ConvertToProcessDataPCA("ENTRENAMENT", numero_components, PCA_VEPS_Orcre_DEC, PCA_numero_components)
d_patients_prediction, class_patients_prediction = patients_prediction.ConvertToProcessDataPCA("TEST", numero_components, PCA_VEPS_Orcre_DEC, PCA_numero_components)
print("")

#
# Classificacio lineal
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

# Entrenamento
print ("Entrenament...")
clases = contar(clasesTrain)
centroides = [calcularCentroides(c) for c in clases.keys()]

# Clasificacion
predicciones = list(map(classify, test))

# Numero de correctos
print ("Prec.:", format(float(len(list(filter(lambda x: x[0] == x[1], zip(*[predicciones, clasesTest]))))) / float(len(test)) * 100.0, '.4f'), '%')
print("")

print ("Temps execucio:",format(clock() - start, '.4f'),"segons")