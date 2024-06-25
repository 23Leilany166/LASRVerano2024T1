def ordenar_asc(datos):
    #Ordenar la longitud de la lista de entrada de los datos
    arr_len = len(datos)
#Visitar la lista 
    for i in range(arr_len):
        min_idx = i
        for j in range(i+1, arr_len):
            if datos[j] < datos[min_idx]:
                min_idx = j
        datos[i], datos[min_idx] = datos[min_idx], datos[i]

    return datos