import pandas as pd
from collections import Counter
#Sirve para

def calcular_limites(datos):

    # Calcular las frecuencias de cada elemento
    frecuencias = Counter(datos)
    
    # Obtener las frecuencias en una lista
    frecuencias_valores = list(frecuencias.values())
    
    # Calcular los límites
    if frecuencias_valores:
        limite_inferior = min(frecuencias_valores)
        limite_superior = max(frecuencias_valores)
    else:
        limite_inferior = None
        limite_superior = None
    
    return limite_inferior, limite_superior
    