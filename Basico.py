import OtroArchivoPython

# La identacion de codigo es importante para la correcta compilacion del codigo
# Identacion con ejemplos: https://www.freecodecamp.org/espanol/news/indentacion-en-python-con-ejemplos/


# string
texto = "Quiero una pizza"

# numero entero
ent = 2

# booleano
datoBooleano = True

# funcion
def convertirIntAstr(numero):
    if(numero):
        numeroConvertido = str(numero)

    return numeroConvertido

# ejecutando funcion
aImprimir = convertirIntAstr(ent)

# imprimir en consola
print(texto + " o " + aImprimir)

# clase
class ClaseAuto:
    def __init__(self, color, marca):
     self.color = color
     self.marca = marca

# objeto instanciado de la clase creada
nuevoAuto = ClaseAuto("rojo", "mercedes")

print(nuevoAuto.marca + " " + nuevoAuto.color)

#imprimimos texto de archivo importado
print(OtroArchivoPython.unaVariableExterna)


