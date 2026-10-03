import pandas as pd
df = pd.read_csv("datos_prueba/ventas.csv")

print("DATA ANALYZER")
print("-------------------")
print("Archivo analizado: ventas.csv")

print("Filas:", df.shape[0])
print("Columnas:", df.shape[1])

print("\nNombres de las columnas:")
print(df.columns)

print("\nTipos de datos:")
print(df.dtypes)

print("\nDatos faltantes:")
print(df.isna().sum())

print("\nDatos duplicados:")
print(df.duplicated().sum())

print("\nCategorias encontradas: ")
print(df["categoria"].unique())

df["categoria_normalizada"] = df["categoria"].str.strip().str.lower()

print("\nCategoria normalizadas:")
print(df["categoria_normalizada"].unique())

print("\nComparacion de categorias:")
print(df[["categoria", "categoria_normalizada"]])

print("\nPrueba de groupby y nunique:")

inconsistencias_categoria = (
    df.groupby("categoria_normalizada")["categoria"]
    .nunique()
)
print(inconsistencias_categoria)

print("\nCategorias con posibles inconsistencias:")

problemas_categoria = inconsistencias_categoria[
    inconsistencias_categoria > 1
]
print(problemas_categoria)