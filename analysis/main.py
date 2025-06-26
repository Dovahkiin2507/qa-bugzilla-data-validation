import pandas as pd

# Cargamos el dataset de bugs corregidos
df = pd.read_csv('../data/fix.csv')

# 1. Mostrar las primeras 5 filas del dataset
print("Primeras filas:")
print(df.head())

# 2. Mostrar dimensiones del dataset (filas x columnas)
print(f"\nDimensiones del dataset: {df.shape[0]} filas y {df.shape[1]} columnas")

# 3. Mostrar nombres de columnas
print("\nColumnas disponibles:")
print(df.columns)

# 4. Ver si hay datos faltantes (NaN)
print("\nDatos faltantes por columna:")
print(df.isna().sum())

# 5. Estadísticas descriptivas
print("\nResumen estadístico de columnas numéricas:")
print(df.describe())

# 6. Conteo de valores únicos por categoría en 'Label'
if 'Label' in df.columns:
    print("\nDistribución de etiquetas (Label):")
    print(df['Label'].value_counts())

# 7. Promedio del tiempo de arreglo de los bugs
if 'Fixing_time' in df.columns:
    print("\nPromedio de tiempo para arreglar un bug:")
    print(df['Fixing_time'].mean())
