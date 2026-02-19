def calcular_iva(precio, impuesto=0.21):
    return precio * (1 + impuesto)

print(f"Total: {calcular_iva(100)}")
