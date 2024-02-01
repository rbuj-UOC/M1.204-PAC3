from math import exp
from time import clock

# declaracio de kernel

def kernelSet(a, b, grau=4):
   da = dict((k,v) for k, v in (l.split(':') for l in a))
   db = dict((k,v) for k, v in (l.split(':') for l in b))
   s = 2 ** sum(min(float(da[key]),float(db[key])) for key in da.keys() if key in db)
   return s**(grau-2)

def kernelSetEXP(a, b, sigma=1):
   return exp(-1 * (((kernelSet(a, a) - 2 * kernelSet(a, b) + kernelSet(b, b)))**0.5) / (2.0 * (2**sigma)))

kernel = kernelSetEXP

# declaracio de funcions

def h(x, tp, tn, cp, cn, b):
   y = (sum([kernel(x, xi) for xi in tp]) / cp -
        sum([kernel(x, xi) for xi in tn]) / cn - b)
   if y > 0:
      return '1'
   else:
      return '-1'

print ("Activitat: 4 (PAC2 / Activitat 1)")
print("")
start = clock()
# carrega de l'arxiu
train = list(map(lambda l: (l.strip()).split(' '),
                 filter(lambda x: x[0] != '#',
                        open('data/activitat1a.train.txt', 'r').readlines())))

# Entrenament
tp = list(filter(lambda x: x[0] == '1', train))
l=list(map(lambda x: x.pop(0), tp))
del(l)
cp = len(tp)

tn = list(filter(lambda x: x[0] == '-1', train))
l=list(map(lambda x: x.pop(0), tn))
del(l)
cn = len(tn)

del(train)

inici = clock()
b = (sum([sum([kernel(xi, xj) for xi in tp])
          for xj in tp]) / (cp ** 2) -
     sum([sum([kernel(xi, xj) for xi in tn])
          for xj in tn]) / (cn ** 2)) / 2
print("Calcul de b:", format(b,".4f"), "en",format(clock() - inici, '.4f'),"segons")

test = list(map(lambda l: (l.strip()).split(' '),
                filter(lambda x: x[0] != '#',
                       open('data/activitat1a.test.txt', 'r').readlines())))
classesTest=list(map(lambda x: x.pop(0), test))

inici = clock()
prediccions = [h(x, tp, tn, cp, cn, b) for x in test]
print("Calcul de h en",format(clock() - inici, '.4f'),"segons")

# Nombre de correctes
correctes=len(list(filter(lambda x: x[0] == x[1], zip(*[prediccions, classesTest]))))
print('Prec.:', format(correctes / float(len(test)) * 100.0, '.4f'), '% ('+str(correctes)+"/"+str(len(test))+")")
print ("Temps execucio:",format(clock() - start, '.4f'),"segons")