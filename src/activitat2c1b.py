from time import clock

import os

start = clock()
print ("Activitat: 2-SVM amb kernel lineal(PAC2 / Activitat 2)")
print ("")

parametros = '-t 0 -c 1'
train = 'data/activitat1b.train.txt'
test  = 'data/activitat1b.test.txt'
model = 'data/activitat2c1b.model.txt'
preds = 'data/activitat2c1b.predicciones.txt'
outs  = 'data/activitat2c1b.output.txt'

print ("Entrenament:")
os.system('/opt/local/bin/svm-train ' + parametros + ' ' + train + ' ' + model)
print ("")

print ("Prediccio:")
os.system('/opt/local/bin/svm-predict ' + test + ' ' + model + ' ' + preds + ' > ' + outs)

print (list(map(lambda l: l.strip(), open(outs, 'r').readlines()))[0])
print("")

print ("Temps execucio:", format(clock() - start, '.4f'), "segons")