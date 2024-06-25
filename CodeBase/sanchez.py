def calcular_frecuencia_relativa(datos):
    
    # Contar la frecuencia absoluta de cada elemento
    frecuencias_absolutas = {}
    for elemento in datos:
        if elemento in frecuencias_absolutas:
            frecuencias_absolutas[elemento] += 1
        else:
            frecuencias_absolutas[elemento] = 1
    
    # Calcular la frecuencia relativa de cada elemento
    total_elementos = len(datos)
    frecuencias_relativas = {}
    for elemento, frecuencia_absoluta in frecuencias_absolutas.items():
        frecuencia_relativa = frecuencia_absoluta / total_elementos
        frecuencias_relativas[elemento] = frecuencia_relativa
    
    return frecuencias_relativas