import matplotlib.pyplot as plt

# Datos de la competencia
competitors = {
    'AgendaPro': {'x': 9, 'y': 9, 'color': '#95a5a6'},  # Alto precio, Alta tec
    'Bewe': {'x': 8, 'y': 8.5, 'color': '#95a5a6'},    # Alto precio, Alta tec
    'Fresha': {'x': 7, 'y': 4, 'color': '#95a5a6'},    # Precio medio (comisiones), Alta tec
    'Excel/Google': {'x': 4, 'y': 1, 'color': '#95a5a6'}, # Bajo precio, Tec media (manual)
    'Cuaderno': {'x': 1, 'y': 0.5, 'color': '#95a5a6'},   # Bajo precio, Baja tec
    'Tiven': {'x': 8.5, 'y': 3, 'color': '#e74c3c'}  # Bajo precio, Alta tec (EL GANADOR)
}

# Configuración del gráfico
plt.figure(figsize=(10, 8))
plt.title('Mapa de Posicionamiento Competitivo - Salones de Belleza', fontsize=16, fontweight='bold')
plt.xlabel('Nivel de Automatización y Digitalización  -->', fontsize=12)
plt.ylabel('Precio / Costo Mensual  -->', fontsize=12)

# Ejes y límites
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid(True, linestyle='--', alpha=0.5)

# Dibujar cuadrantes
plt.axhline(y=5, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=5, color='k', linestyle='-', alpha=0.3)

# Etiquetas de los cuadrantes
plt.text(1, 9.5, 'Caro y Manual\n(Ineficiente)', fontsize=10, color='gray')
plt.text(9, 9.5, 'Caro y Tecnológico\n(Corporativo)', fontsize=10, color='gray', ha='right')
plt.text(1, 0.5, 'Barato y Manual\n(Tradicional)', fontsize=10, color='gray')
plt.text(9, 0.5, 'Barato y Tecnológico\n(Oportunidad Tiven)', fontsize=10, color='green', fontweight='bold', ha='right')

# Plotear puntos
for name, data in competitors.items():
    plt.scatter(data['x'], data['y'], s=200, c=data['color'], edgecolors='black', alpha=0.8)
    plt.text(data['x'], data['y']+0.3, name, fontsize=11, fontweight='bold', ha='center')

# Guardar
filename = 'Mapa_Competencia_Tiven.png'
plt.savefig(filename)
print(filename)