mes = "agosto"
#la coma es un espacio
print("el mes es:", mes)

dia = 16

print("el dia", dia, "del mes", mes)

alumnos = 23
grupo = 9

print("los alumnos son {} y son del grupo {} y todos estan atentos".format(
    alumnos, grupo))

#para que no se cambien los valores colocamos en las {} la posicion del array(grupo(posicion 0), alumnos(posicion 1))
print("los alumnos son {1} y son del grupo {0} y todos estan atentos".format(
    grupo, alumnos))

#print(f) el f es el format y cuando va al comienzo significa que lo que va en las {} es codigo puro de python
#print(f"los alumnos son {alumnos} {1+5}")
print(f"los alumnos son {alumnos}")