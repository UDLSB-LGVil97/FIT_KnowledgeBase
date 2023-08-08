import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



st.set_page_config(
    page_title="Cars dataframe",
    page_icon="📊",
)

st.markdown("# Dataframe demo")
st.sidebar.header("📊 Dataframe demo")
st.write("""
    Esta demo ilustra el funcionamiento de presentación
    de un dataframe para fines de visualización de bases
    de datos, o bien, de datasets para machine learning.
""")



# Cargar datos de ejemplo (reemplaza esto con tu propio archivo CSV)
data = pd.DataFrame({
    'Marca': ['Toyota', 'Honda', 'Nissan', 'Ford', 'Chevrolet', 'Toyota', 'Ford', 'Honda'],
    'Modelo': ['Corolla', 'Civic', 'Sentra', 'Focus', 'Cruze', 'Camry', 'Mustang', 'Accord'],
    'Año': [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'Precio': [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000]
})

# Crear la aplicación Streamlit
st.title("Dashboard de Vehículos")

# Mostrar estadísticas básicas
st.write(data.describe())

# Filtro de marcas
selected_brand = st.sidebar.selectbox("Selecciona una marca", sorted(data['Marca'].unique()))

# Filtro de año
min_year, max_year = int(data['Año'].min()), int(data['Año'].max())
year_range = st.sidebar.slider("Selecciona el rango de años", min_year, max_year, (min_year, max_year))

# Filtrar los datos según la selección del usuario
filtered_data = data[(data['Marca'] == selected_brand) & (data['Año'] >= year_range[0]) & (data['Año'] <= year_range[1])]

# Mostrar datos filtrados
st.subheader(f"Vehículos de la marca {selected_brand} en el rango de años {year_range}")
st.write(filtered_data)

# Crear un gráfico de barras de precios por modelo
price_chart = sns.barplot(x='Modelo', y='Precio', data=filtered_data)
plt.xlabel("Modelo")
plt.ylabel("Precio")
plt.title(f"Precios de los modelos {selected_brand} en el rango de años {year_range}")
st.pyplot(price_chart.figure)