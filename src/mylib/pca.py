from mylib.utilitats import *

def GetPCA(d, percentatge):
    A, centroides, matriu_autocorrelacio = Analisi_Multivariable(d)

    # Obtenir els valors singulars
    valors_Propis, vectors_Propis = Descomposicio_Valors_Singulars(matriu_autocorrelacio)

    # Obtenir els valors propis ordenats per ordre decreixent
    indexs_creixent = argsort(valors_Propis)  # orden creciente
    indexs_decreixent = indexs_creixent[::-1] # orden decreciente
    valors_Propis_OrdreDecreixent = valors_Propis[indexs_decreixent] # valores propios en orden decreciente
    vectors_Propis_OrdreDecreixent = vectors_Propis[:,indexs_decreixent] # valores propios en orden decreciente

    # determinar el nombre necessari de components per obtenir un 95% de variancia
    valors_Propis_suma = sum(valors_Propis)
    numero_components = 1
    while ((sum(valors_Propis_OrdreDecreixent[:numero_components]) / valors_Propis_suma) < percentatge):
        numero_components += 1
    print ("Es requereixen", numero_components, "components per obtenir un", (sum(valors_Propis_OrdreDecreixent[:numero_components]) / valors_Propis_suma) * 100, "% de variancia")

    # retornar els indexs de les variables
    llista_variables=[]
    for num_variable in range(numero_components):
        llista_variables.append(indexs_decreixent[num_variable])
    return llista_variables, vectors_Propis_OrdreDecreixent

def ProyectPCA(d, PCA_VEPS_Orcre_DEC, numero_components):
    A, centroides, matriu_autocorrelacio = Analisi_Multivariable(d)
    d_PCA = zeros((d.shape[0], numero_components), float)
    for i in range(d_PCA.shape[0]):
        for j in range(d_PCA.shape[1]):
            d_PCA[i, j] = dot(A[i, :], PCA_VEPS_Orcre_DEC[:, j])
    return d_PCA
