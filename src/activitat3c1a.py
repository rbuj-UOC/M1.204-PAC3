from time import clock
import os

start = clock()
print ("Activitat: 3-SVM amb kernel radial amb diferents gammes i C (PAC2 / Activitat 1)")
print ("")

train = 'data/activitat1a.train.txt'
test  = 'data/activitat1a.test.txt'

resultats_proves=[]
for exp in range(-4,5,1):
    for gamma in range(-4,5,1):
        resultats_prova=[]
        model = 'data/activitat3c1a.'+str(10**exp)+'.'+str(10**exp)+'.model.txt'
        preds = 'data/activitat3c1a.'+str(10**exp)+'.'+str(10**exp)+'.predicciones.txt'
        outs  = 'data/activitat3c1a.'+str(10**exp)+'.'+str(10**exp)+'.output.txt'
        parametros = '-q -t 2 -g '+str(10**gamma)+' -c '+str(10**exp)
        resultats_prova.append(10**gamma)
        resultats_prova.append(10**exp)
        resultats_prova.append(clock())
        os.system('/opt/local/bin/svm-train ' + parametros + ' ' + train + ' ' + model)
        resultats_prova.append(clock())
        os.system('/opt/local/bin/svm-predict ' + test + ' ' + model + ' ' + preds + ' > ' + outs)
        resultats_prova.append(clock())
        resultats_prova.append(list(map(lambda l: l.strip(), open(outs, 'r').readlines()))[0])
        resultats_proves.append(resultats_prova)

print("------------------------------------------------------------------------")
print(" Resultats obtinguts ordenats per C")
print("------------------------------------------------------------------------")
print ("Gamma".rjust(10),"C".rjust(12), "  T.Entrenament".ljust(15), " T.Prediccio".ljust(15), "P.Prediccio")
for resultats_prova in sorted(resultats_proves, key=lambda resultats_proves: resultats_proves[1]):
    text_percentatge = resultats_prova[5].split()
    print (format(resultats_prova[0], '.4f').rjust(10)," ",
        format(resultats_prova[1], '.4f').rjust(10)," ",
        format(resultats_prova[3]-resultats_prova[2], '.4f'),"segons ",
        format(resultats_prova[4]-resultats_prova[3], '.4f'),"segons ",
        text_percentatge[2].ljust(8), text_percentatge[3])
print("------------------------------------------------------------------------")
print("")

print("------------------------------------------------------------------------")
print(" Resultats obtinguts ordenats per Gamma")
print("------------------------------------------------------------------------")
print ("Gamma".rjust(10),"C".rjust(12), "  T.Entrenament".ljust(15), " T.Prediccio".ljust(15), "P.Prediccio")
for resultats_prova in sorted(resultats_proves, key=lambda resultats_proves: resultats_proves[0]):
    text_percentatge = resultats_prova[5].split()
    print (format(resultats_prova[0], '.4f').rjust(10)," ",
        format(resultats_prova[1], '.4f').rjust(10)," ",
        format(resultats_prova[3]-resultats_prova[2], '.4f'),"segons ",
        format(resultats_prova[4]-resultats_prova[3], '.4f'),"segons ",
        text_percentatge[2].ljust(8), text_percentatge[3])
print("------------------------------------------------------------------------")
print("")

print("------------------------------------------------------------------------")
print(" Resultats obtinguts ordenats per P.Prediccio")
print("------------------------------------------------------------------------")
print ("Gamma".rjust(10),"C".rjust(12), "  T.Entrenament".ljust(15), " T.Prediccio".ljust(15), "P.Prediccio")
for resultats_prova in sorted(resultats_proves, key=lambda resultats_proves: resultats_proves[5]):
    text_percentatge = resultats_prova[5].split()
    print (format(resultats_prova[0], '.4f').rjust(10)," ",
        format(resultats_prova[1], '.4f').rjust(10)," ",
        format(resultats_prova[3]-resultats_prova[2], '.4f'),"segons ",
        format(resultats_prova[4]-resultats_prova[3], '.4f'),"segons ",
        text_percentatge[2].ljust(8), text_percentatge[3])
print("------------------------------------------------------------------------")
