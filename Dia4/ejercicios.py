# segun la libreria camelcase que convierte cada inicio de palabra en mayuscula hacer lo mismo pero sin la libreria usando el codigo ascii

# si el texto de ingreso es:
texto = "hola alumnos buenas noches ya se viene el break"
# entonces el texto resultado debera ser:
resultado_final = ["Hola", "Alumnos", "Buenas", "Noches", "Ya", "Se"]


palabras = texto.split()
print(palabras)

p1 = palabras[0].replace('h',chr(72),1)
p2 = palabras[1].replace('a',chr(65),1)
p3 = palabras[2].replace("b", chr(66),1)
p4 = palabras[3].replace("n", chr(78),1)
p5 = palabras[4].replace("y", chr(89),1)
p6 = palabras[5].replace("s", chr(83),1)
p7 = palabras[6].replace("v", chr(86),1)
p8 = palabras[7].replace("e", chr(69),1)
p8 = palabras[8].replace("b", chr(66),1)

print(f"{p1} {p2} {p3} {p4} {p5} {p6} {p7} {p8}")

ptotal = p1+" "+p2+" "+p3+" "+p4+" "+p5+" "+p6+" "+ p7+" "+p8

textof = ptotal.split()
print(textof)


# for letra in texto:
#     print(letra, (chr(95+9) == chr(72)))

# # asi se saca la ubicacion del caracter usando Codigo ASCII
print(ord("x"))

# print(chr(95+15))

