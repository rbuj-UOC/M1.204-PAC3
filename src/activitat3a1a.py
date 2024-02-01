from time import clock
import os

start = clock()
print ("Activitat: 3-SVM amb kernel lineal amb C vble (PAC2 / Activitat 1)")
print ("")

train = 'data/activitat1a.train.txt'
test  = 'data/activitat1a.test.txt'

resultats_proves=[]
for exp in range(-4,5,1):
    resultats_prova=[]
    model = 'data/activitat3a1a.'+str(10**exp)+'.model.txt'
    preds = 'data/activitat3a1a.'+str(10**exp)+'.predicciones.txt'
    outs  = 'data/activitat3a1a.'+str(10**exp)+'.output.txt'
    parametros = '-t 0 -q -c '+str(10**exp)
    resultats_prova.append(10**exp)
    resultats_prova.append(clock())
    os.system('/opt/local/bin/svm-train ' + parametros + ' ' + train + ' ' + model)
    resultats_prova.append(clock())
    os.system('/opt/local/bin/svm-predict ' + test + ' ' + model + ' ' + preds + ' > ' + outs)
    resultats_prova.append(clock())
    resultats_prova.append(list(map(lambda l: l.strip(), open(outs, 'r').readlines()))[0])
    resultats_proves.append(resultats_prova)

print ("C".rjust(10), "  T.Entrenament".ljust(15), " T.Prediccio".ljust(15), "P.Prediccio")
for resultats_prova in resultats_proves:
    text_percentatge = resultats_prova[4].split()
    print (format(resultats_prova[0], '.4f').rjust(10)," ",
        format(resultats_prova[2]-resultats_prova[1], '.4f'),"segons ",
        format(resultats_prova[3]-resultats_prova[2], '.4f'),"segons ",
        text_percentatge[2].ljust(8), text_percentatge[3])