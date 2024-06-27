import matplotlib.pyplot as plt

colors = ["#F8BBD0", "#D1C4E9", "#B2EBF2", "#C8E6C9"]

# HISTOGRAMA
def Histograma(marcasClase, fr, titulo="Histograma", colores=colors):
    plt.figure(figsize = (8, 4))
    valores_ref_eje = list(range(1, len(marcasClase) + 1))
    plt.bar(valores_ref_eje, fr,
            width = 1, edgecolor= "k", 
            color = colores) 
    plt.xticks(valores_ref_eje, marcasClase, fontsize = 10)
    plt.xlabel("Marcas de clase", fontsize = 15)
    plt.ylabel("Frecuencia Absoluta", fontsize = 15)
    plt.title(titulo, fontsize = 20)
    plt.grid()
    plt.show()

# DIAGRAMA DE BARRAS
def Diagrama_Barras(marcasClase, fa, titulo="Diagrama de barras", colores=colors):
    plt.figure(figsize = (8, 4)) 
    valores_ref_eje = list(range(1, len(marcasClase) + 1))
    plt.barh(valores_ref_eje, fa,
            height = 0.8, edgecolor= "k", 
            color = colores) 

    plt.gca().invert_yaxis() 
    plt.yticks(valores_ref_eje, marcasClase, fontsize = 10) 
    plt.xlabel("Frecuencia absoluta ", fontsize = 15)
    plt.ylabel("Marcas de clase", fontsize = 15) 
    plt.title(titulo, fontsize = 20) 
    plt.grid() 
    plt.show() 

# GRAFICA DE PASTEL
def Diagrama_pastel(marcasClase, fa, fr, titulo="Diagrama de pastel", colores=colors):
    if 'separaciones' in locals() or 'separaciones' in globals():
        if len(separaciones) == 0:
            print("The list exists and is empty.")
            separaciones = [0] * len(fa)
        else:
            print("The list exists and is not empty.")
    else:
        separaciones = [0] * len(fa)
    
    plt.figure(figsize = (10, 6)) 
    plt.pie(fr,
            explode = separaciones,
            colors = colores,
            pctdistance = .8,
            counterclock = False,
            startangle = 90,
            autopct = "%0.1f%%",
            labels = marcasClase)
    plt.title(titulo, fontsize = 20) 
    plt.show()

# POLÍGONO DE FRECUENCIAS
def Poligono_Frecuencia(marcasClase, fr, titulo="Polígono de frecuencias", colores=colors):
    plt.figure(figsize = (15, 5))
    valores_ref_eje = list(range(1, len(marcasClase) + 1))
    datos_x = [0] + valores_ref_eje + [valores_ref_eje[-1] + 1]
    datos_y = [0] + fr + [0]

    plt.plot(datos_x, datos_y, 
         linewidth = 3, 
         color = "#C8E6C9", 
         linestyle = "--", 
         marker = "o", 
         markersize = 10, 
         markerfacecolor = "#ADD8E6",
         markeredgecolor = "#B0C4DE",
         markeredgewidth = 1.5) 

    plt.xticks(valores_ref_eje, marcasClase, fontsize = 10)  
    plt.xlabel("Marcas de clase", fontsize = 15) 
    plt.ylabel("Frecuencia relativa", fontsize = 15) 
    plt.title(titulo, fontsize = 20) 
    plt.grid() 
    plt.show() 

# OJIVA
def Ojiva(marcasClase, frAcum, titulo="Ojiva", colores=colors):
    plt.figure(figsize = (15, 5))
    valores_ref_eje = list(range(1, len(marcasClase) + 1))
    datos_x = [0] + valores_ref_eje
    datos_y = [0] + frAcum

    plt.plot(datos_x, datos_y, 
        linewidth = 3, 
        color = "#87CEEB", 
        linestyle = "--",
        marker = "o",
        markersize = 10,
        markerfacecolor = "#ADD8E6", 
        markeredgecolor = "#B0C4DE",
        markeredgewidth = 1.5) 

    plt.xticks(valores_ref_eje, marcasClase, fontsize = 10, )
    plt.xlabel("Marcas de clase", fontsize = 15) 
    plt.ylabel("Frecuencia acumulada", fontsize = 15)
    plt.title(titulo, fontsize = 20) 
    plt.grid() 
    plt.show()


def displayCharts(marcasClase, fa, fr, frAcum):
    Histograma(marcasClase, fa)
    Diagrama_Barras(marcasClase, fa)
    Diagrama_pastel(marcasClase, fa, fr)
    Poligono_Frecuencia(marcasClase,fr)
    Ojiva(marcasClase, frAcum)