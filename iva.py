def calcular_total_con_iva(precio):
    # Esta es la validación de seguridad
    if precio < 0:
        return "Error: El precio no puede ser negativo"
    
    iva = 0.21
    return precio * (1 + iva)

# Prueba del sistema con un valor erróneo para verificar
precio_articulo = -50 
resultado = calcular_total_con_iva(precio_articulo)
print(f"Resultado del sistema: {resultado}")
