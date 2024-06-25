def frec_abs(datos):
    clases, fa_absoluta = [], []
    for elemento in datos:
        if elemento not in clases:
            clases.append(elemento)
            fa_absoluta.append(1)
        else:        
            idx = clases.index(elemento)        
            fa_absoluta[idx] += 1
    return clases, fa_absoluta  