texto = "Python es un lenguaje muy util de programación, Python es muy bueno".lower()
palabras = texto.split()

conteo = {}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
        
        
for palabra, cantidad in conteo.items():
    print(f"{palabra}: {cantidad}: veces")