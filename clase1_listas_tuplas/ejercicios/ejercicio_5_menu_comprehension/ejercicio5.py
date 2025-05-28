precios= [2000, 5000, 10000, 20000, 50000]

precios_iva = [round(precio*1.19,2) for precio in precios]
print(precios_iva)