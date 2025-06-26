# Análisis de Errores en Mozilla Firefox

Este proyecto analiza errores reportados en Mozilla Firefox, con el objetivo de identificar patrones que puedan ayudar a mejorar la eficiencia en su resolución. La fuente de datos corresponde a registros históricos de bugs clasificados por severidad y tiempo de corrección.

## 🎯 Objetivo

Obtener información útil a partir del análisis de bugs resueltos, diferenciando entre errores críticos y no críticos, para extraer conclusiones que puedan servir a equipos de desarrollo o QA.

## 📁 Estructura del Proyecto

📦qa-bugzilla-data-validation
┣ 📂analysis
┃ ┣ 📜main.py → análisis exploratorio del dataset
┃ ┗ 📜visualitation.py → visualización de datos
┣ 📂data
┃ ┗ 📜fix.csv → dataset principal utilizado
┗ 📜README.md


## 📊 Principales Resultados

- Se analizaron **32.428 registros** de bugs corregidos.
- El 23.5% de los bugs fueron clasificados como **críticos**.
- El tiempo promedio de corrección fue de **184 minutos**, pero los errores críticos tienden a requerir mucho más tiempo de resolución que los no críticos.
- Se utilizaron gráficos de barra y boxplot para visualizar las diferencias en cantidad y tiempo de corrección según la severidad del error.

## 🔧 Tecnologías utilizadas

- Python 3
- Pandas
- Matplotlib
- Seaborn
- PyCharm

## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio:
   ```
   git clone https://github.com/tu_usuario/nombre_del_repo.git
   ```
2. Instala las dependencias:
   ```
   pip install pandas matplotlib seaborn
   ```
3. Ejecuta los scripts desde la raíz del proyecto:
   ```
   python analysis/main.py
   python analysis/visualitation.py
   ```
## ✅ Conclusiones
Este pequeño análisis confirma que los bugs críticos, aunque menos frecuentes, requieren mucho más tiempo de corrección. Esto puede ayudar a priorizar tareas dentro de un equipo de QA o desarrollo, y sugiere que invertir tiempo en prevenir bugs críticos puede ser muy rentable a largo plazo.

