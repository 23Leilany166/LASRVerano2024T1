from collections import Counter
import pandas as pd
def calcular_rango(datos):

    # Calcular las frecuencias de cada elemento
    frecuencias = Counter(datos)
    
    # Obtener las frecuencias en una lista
    frecuencias_valores = list(frecuencias.values())
    
    # Calcular el rango
    if frecuencias_valores:
        rango = max(frecuencias_valores) - min(frecuencias_valores)
    else:
        rango = None
    
    return rango
