import matplotlib.pyplot as plt

# Datos de la competencia KOFINET
competitors_cafe = {
    'Soft Restaurant': {'x': 2, 'y': 8, 'color': '#95a5a6'},  # Lento y Caro (Licencia alta)
    'Poster POS': {'x': 8, 'y': 9, 'color': '#95a5a6'},       # Rápido pero Caro (Renta mensual)
    'Loyverse': {'x': 7, 'y': 1, 'color': '#95a5a6'},         # Rápido y Barato (Pero limitado en funciones)
    'Kofinet': {'x': 9, 'y': 3, 'color': '#e67e22'}      # Muy Rápido y Precio Accesible (El Ganador)
}

# Configuración del gráfico
plt.figure(figsize=(10, 8))
plt.title('Mapa de Competencia - Sistemas para Cafeterías (QSR)', fontsize=16, fontweight='bold')
plt.xlabel('Velocidad de Servicio y Enfoque "To Go"  -->', fontsize=12)
plt.ylabel('Costo a Largo Plazo (Rentas o Licencias)  -->', fontsize=12)

# Ejes y límites
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid(True, linestyle='--', alpha=0.5)

# Dibujar cuadrantes
plt.axhline(y=5, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=5, color='k', linestyle='-', alpha=0.3)

# Etiquetas de los cuadrantes
plt.text(1, 9.5, 'Lento y Caro\n(Restaurantes de Mesa)', fontsize=10, color='gray')
plt.text(9, 9.5, 'Rápido pero Renta\n(SaaS Nube)', fontsize=10, color='gray', ha='right')
plt.text(1, 0.5, 'Lento y Barato\n(Manual/Excel)', fontsize=10, color='gray')
plt.text(9, 0.5, 'KOFINET\n(Velocidad + Pago Único)', fontsize=12, color='#d35400', fontweight='bold', ha='right')

# Plotear puntos
for name, data in competitors_cafe.items():
    plt.scatter(data['x'], data['y'], s=250, c=data['color'], edgecolors='black', alpha=0.8)
    plt.text(data['x'], data['y']+0.4, name, fontsize=11, fontweight='bold', ha='center')

# Guardar
filename = 'Mapa_Competencia_Kofinet_Final.png'
plt.savefig(filename)
print(filename)