def frec_abs(datos):
    clases, fa_absoluta = [], []
    for elemento in datos:
        if elemento not in clases:
            clases.append(elemento)
            fa_absoluta.append(1)
        else:
            idx = clases.index(elemento)
            fa_absoluta[idx] += 1

    # Ordenar fa_absoluta y clases de acuerdo a fa_absoluta
    fa_absoluta_sorted = sorted(fa_absoluta)
    clases_sorted = [clases[i]
                     for i in sorted(range(len(fa_absoluta)), key=lambda k: fa_absoluta[k])]

    return clases_sorted, fa_absoluta_sorted

#En resumen, key=lambda te permite definir un criterio personalizado de ordenamiento
# que se aplica a cada elemento de la lista antes de determinar su posición en el resultado final.