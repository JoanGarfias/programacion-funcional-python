import matplotlib.pyplot as plt
import numpy as np

# Datos basados en la proyección "Realista/Conservadora" de DxiCode
meses = np.arange(1, 13)
# Ingresos mensuales (Ramp-up progresivo hasta 122k)
ventas = np.array([0, 0, 2100, 7900, 13400, 21000, 33500, 45800, 59000, 78000, 99500, 122800])

# Costos
costos_fijos = 36000 # Optimizado
costos_variables_aprox = ventas * 0.15 # Estimado 15% (Pasarelas + Server)
costos_totales = costos_fijos + costos_variables_aprox

# Flujo de Caja
flujo_mensual = ventas - costos_totales
inversion_inicial = 110000 
flujo_acumulado = np.cumsum(flujo_mensual) - inversion_inicial

# Configuración de Gráficas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# GRÁFICA 1: PUNTO DE EQUILIBRIO
ax1.plot(meses, costos_fijos * np.ones_like(meses), 'r--', label='Costos Fijos ($36k)', alpha=0.6)
ax1.plot(meses, costos_totales, 'r-', linewidth=2, label='Costos Totales')
ax1.plot(meses, ventas, 'g-', linewidth=3, label='Ventas Totales')

# Encontrar cruce visual
cruce_mes = 7.5 # Visual aprox
ax1.annotate('¡Punto de Equilibrio!', xy=(cruce_mes, 40000), xytext=(4, 80000),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold')

ax1.set_title('Punto de Equilibrio (Break-even)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Meses de Operación')
ax1.set_ylabel('Dinero (MXN)')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.5)

# GRÁFICA 2: RETORNO DE INVERSIÓN (CASH FLOW)
colores = ['red' if x < 0 else 'green' for x in flujo_mensual]
ax2.bar(meses, flujo_mensual, color=colores, alpha=0.7, label='Utilidad/Pérdida Mensual')
ax2.plot(meses, flujo_acumulado, 'b-o', linewidth=2, label='Recuperación Inversión (Acumulado)')

# Línea cero
ax2.axhline(0, color='black', linewidth=1)

ax2.set_title('Retorno de Inversión y Flujo de Caja', fontsize=14, fontweight='bold')
ax2.set_xlabel('Meses de Operación')
ax2.set_ylabel('Utilidad Neta (MXN)')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
filename = 'Graficas_Financieras_DxiCode.png'
plt.savefig(filename)
print(filename)