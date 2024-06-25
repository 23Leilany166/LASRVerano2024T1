def format_str(datos):
    d_formated = []
    for dato in datos:
        if isinstance(dato, str):
            #Str sirve para trabajar con todo tipo de datos de texto para crear, manipular, formatear y procesar cadenas
            # de texto de manera eficiente.
            dato_formateado = dato.upper().replace(" ", "")
            d_formated.append(dato_formateado)
        else:
            d_formated.append(dato)
    return d_formated