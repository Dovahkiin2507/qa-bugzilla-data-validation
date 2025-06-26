import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('../data/fix.csv')

# Estilo visual
sns.set(style="whitegrid")

# Conteo de bugs por severidad (Label)
plt.figure(figsize=(6, 4))
sns.countplot(x='Label', data=df, palette='Set2')
plt.title('Distribución de Bugs por Severidad')
plt.xlabel('Label (0 = No Crítico, 1 = Crítico)')
plt.ylabel('Cantidad')
plt.tight_layout()

# Mostrar gráfico
plt.show()

# Gráfico de distribución del tiempo de arreglo por tipo de bug
plt.figure(figsize=(8, 5))
sns.boxplot(x='Label', y='Fixing_time', data=df, palette='Set3')
plt.title('Tiempo de Arreglo por Severidad del Bug')
plt.xlabel('Label (0 = No Crítico, 1 = Crítico)')
plt.ylabel('Tiempo de Arreglo (minutos)')
plt.ylim(0, 1000)  # Limitar el eje Y para que no se distorsione por valores extremos
plt.tight_layout()

# Mostrar gráfico
plt.show()
