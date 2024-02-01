from numpy import *

def Mitja_Aritmetica(d):
    resultat = zeros(d.shape[1])
    for i in range(d.shape[1]):
        resultat[i] = sum(d[:, i]) / d.shape[0]
    return resultat

def Analisi_Multivariable(d):
    centroides = d.mean(0) # centroides = mitja_Aritmetica(d)
    A = d - centroides
    matriu_autocorrelacio = dot(A.T, A)
    return A, centroides, matriu_autocorrelacio

def Descomposicio_Valors_Singulars(matcov):
    return linalg.eig(matcov)
