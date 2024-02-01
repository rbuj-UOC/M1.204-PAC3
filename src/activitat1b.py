from mylib.arithmetic_mean import arithmeticMean
from mylib.class_patient import Patient
from mylib.class_patients import Patients
from numpy import *
from time import clock

def write2file(filename, datos, clase):
    with open(filename, 'w') as f:
        for elem_classe, d in zip(clase, datos):
            i = iter(d)
            c = dict(zip(range(len(d)), i))
            f.write(str((-1)**elem_classe[0]))
            for key in c.keys():
                f.write(" "+str(key)+":"+str(c[key]))
            f.write('\n')

start = clock()
print ("Activitat: 1 (PAC2 / Activitat 2)")
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

print ("> Prediccio <")
print ("Nombre de pacients prediccio:", patients_prediction.Size())
patients_prediction.SetFixedValues(patients_train.GetFixedValues())
patients_prediction.SetRang(patients_train.GetRang())
patients_prediction.Fix()
print("")

#
# PCA: trobar quines variables proporcionen un 95% de varianca amb els  pacients
#      d'entrenament
#
print ("Analisi PCA:")
PCA_VEPS_Orcre_DEC, PCA_numero_components = patients_train.GetPCA(numero_components, 0.95)
d_patients_train, class_patients_train = patients_train.ConvertToProcessDataPCA("ENTRENAMENT", numero_components, PCA_VEPS_Orcre_DEC, PCA_numero_components)
d_patients_prediction, class_patients_prediction = patients_prediction.ConvertToProcessDataPCA("TEST", numero_components, PCA_VEPS_Orcre_DEC, PCA_numero_components)
print("")

print ("Volcant dades a fitxers:")
print ("< Entrenament")
write2file('data/activitat1b.train.txt', d_patients_train, class_patients_train)
print ("< Prediccio")
write2file('data/activitat1b.test.txt', d_patients_prediction, class_patients_prediction)
print("")

print ("Temps execucio:",format(clock() - start, '.4f'),"segons")