# 🏎️ Análisis de Fórmula 1 con PySpark

Este proyecto aplica técnicas de procesamiento distribuido con PySpark para analizar datos históricos del Campeonato Mundial de Fórmula 1. Utiliza un conjunto de datos real extraído de Kaggle y permite realizar análisis por temporada, escudería, piloto y circuito.

---

## 📁 Estructura del proyecto

```
f1-pyspark-analysis/
├── data/              # Archivos CSV descargados desde Kaggle
├── notebooks/         # (Opcional) Notebooks para pruebas
├── scripts/           # Scripts en PySpark para análisis
├── README.md          # Este archivo
└── requirements.txt   # Dependencias del entorno
```

---

## 🔧 Requisitos

- Python 3.8+
- Apache Spark
- PySpark
- pandas (para postprocesamiento)

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

---

## 📦 Dataset utilizado

[F1 World Championship (1950 - 2020) - Kaggle](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)

Coloca los siguientes archivos CSV dentro de la carpeta `/data`:

- `results.csv`
- `races.csv`
- `drivers.csv`
- `constructors.csv`

---

## 🚀 Scripts incluidos

### 🔹 `analisis_inicial.py`
Carga y visualiza los datos base:
- Muestra columnas y registros del dataset.
- Agrupa resultados por escudería.

### 🔹 `analisis_avanzado.py`
Análisis detallado:
- Joins entre múltiples tablas (races, drivers, constructors, results).
- Filtrado por temporada.
- Ranking de pilotos por puntos en un año.
- Carreras disputadas por escudería.

---

## 🎯 Objetivos del proyecto

- Practicar el uso de PySpark y Spark SQL.
- Entender cómo trabajar con grandes volúmenes de datos estructurados.
- Aplicar análisis de datos a un tema apasionante como la F1.

---

## 🤝 Contribuciones

Este proyecto es personal y está en evolución. Se aceptan ideas, mejoras o pull requests.

---

## 📬 Contacto

Creado por **Agustín Jesús Capafons Pérez**  
📧 [ajcapafonsp@gmail.com](mailto:ajcapafonsp@gmail.com)
