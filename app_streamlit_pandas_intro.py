
import streamlit as st
import pandas as pd
import numpy as np

st.markdown("<h1 style='text-align: center;'>📘 Introducción a Pandas y Tratamiento de NaN</h1>", unsafe_allow_html=True)
st.markdown("""
Este informe interactivo presenta los fundamentos del uso de Pandas y Numpy en Python, incluyendo Series,
creación de DataFrames y el tratamiento de valores faltantes (`NaN`) mediante diferentes estrategias.
""")

# --- Series de Pandas ---
st.header("1️⃣ Series de Pandas")
st.code("""
import pandas as pd
serie = pd.Series([10, 20, 30, 40, 50])
print(serie)
""")
serie = pd.Series([10, 20, 30, 40, 50])
st.write(serie)

# --- DataFrame simple ---
st.header("2️⃣ Creación de un DataFrame")
st.code("""
datos = {
    "Producto": ["Carro", "Moto", "Avion"],
    "Precio": [300, 200, 700],
    "Cantidad": [10, 20, 5]
}
df = pd.DataFrame(datos)
print(df.head())
print(df.tail())
print("Dimensión:", df.shape)
print("Tipos de datos:\n", df.dtypes)
""")
datos = {
    "Producto": ["Carro", "Moto", "Avion"],
    "Precio": [300, 200, 700],
    "Cantidad": [10, 20, 5]
}
df = pd.DataFrame(datos)
st.dataframe(df)
st.text(f"Dimensión: {df.shape}")
st.text(f"Tipos de datos:\n{df.dtypes}")

# --- DataFrame con NaN ---
st.header("3️⃣ Introducción a NaN con NumPy + Pandas")
st.code("""
precios = np.array([100, 200, np.nan, 400, 500])
cantidades = np.array([10, np.nan, 30, np.nan, 50])

datos_nuevos = {
    "Producto": ["Carro", "Moto", "Avion", "Barco", "Tren"],
    "Precio": precios,
    "Cantidad": cantidades
}
df = pd.DataFrame(datos_nuevos)
print(df)
print(df.isna().sum())
""")
precios = np.array([100, 200, np.nan, 400, 500])
cantidades = np.array([10, np.nan, 30, np.nan, 50])
datos_nuevos = {
    "Producto": ["Carro", "Moto", "Avion", "Barco", "Tren"],
    "Precio": precios,
    "Cantidad": cantidades
}
df = pd.DataFrame(datos_nuevos)
st.dataframe(df)
st.write("Valores faltantes por columna:")
st.write(df.isna().sum())

# --- Tratamiento de valores faltantes ---
st.header("4️⃣ Tratamiento de NaN")
st.subheader("Eliminar filas/columnas con NaN")
st.code("""
df_sin_nan = df.dropna()
df_sin_columnas_nan = df.dropna(axis=1)
""")
st.write("Eliminar filas con al menos un NaN:")
st.dataframe(df.dropna())
st.write("Eliminar columnas con al menos un NaN:")
st.dataframe(df.dropna(axis=1))

st.subheader("Reemplazo por 0, media, mediana, moda")
df_cero = df.copy()
df_cero["Precio"] = df_cero["Precio"].fillna(0)
df_cero["Cantidad"] = df_cero["Cantidad"].fillna(0)

df_media = df.copy()
df_media["Precio"] = df_media["Precio"].fillna(df_media["Precio"].mean())
df_media["Cantidad"] = df_media["Cantidad"].fillna(df_media["Cantidad"].mean())

df_mediana = df.copy()
df_mediana["Precio"] = df_mediana["Precio"].fillna(df_mediana["Precio"].median())
df_mediana["Cantidad"] = df_mediana["Cantidad"].fillna(df_mediana["Cantidad"].median())

df_moda = df.copy()
df_moda["Precio"] = df_moda["Precio"].fillna(df_moda["Precio"].mode()[0])
df_moda["Cantidad"] = df_moda["Cantidad"].fillna(df_moda["Cantidad"].mode()[0])

st.code("""
df["Precio"].fillna(0)
df["Precio"].fillna(df["Precio"].mean())
df["Precio"].fillna(df["Precio"].median())
df["Precio"].fillna(df["Precio"].mode()[0])
""")
st.write("🔹 Relleno con 0")
st.dataframe(df_cero)
st.write("🔹 Relleno con media")
st.dataframe(df_media)
st.write("🔹 Relleno con mediana")
st.dataframe(df_mediana)
st.write("🔹 Relleno con moda")
st.dataframe(df_moda)
