# 🏎️ Análisis de Fórmula 1 con PySpark

Proyecto personal para practicar procesamiento de datos con **PySpark** sobre información histórica de Fórmula 1. Parte de datos tabulares en CSV y construye análisis mediante joins, filtros y agregaciones con Spark SQL.

No pretende ser una plataforma de datos de producción: es una pieza de aprendizaje práctica y reproducible para consolidar fundamentos de ingeniería de datos.

## Qué analiza

- Resultados, carreras, pilotos y constructores.
- Rankings de pilotos por puntos en una temporada.
- Número de carreras disputadas por escudería.
- Relaciones entre varias tablas mediante joins.

## Tecnologías

- Python
- Apache Spark / PySpark
- Spark SQL
- CSV

## Estructura

```text
f1-pyspark-analysis/
├── data/                     # Dataset de F1 en CSV
├── scripts/
│   ├── analisis_inicial.py   # Carga y exploración básica
│   └── analisis_avanzado.py # Joins, filtros y agregaciones
├── requirements.txt
└── README.md
```

## Dataset

El proyecto utiliza el dataset público [Formula 1 World Championship](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020) de Kaggle.

Para ejecutar los scripts, descarga los CSV y colócalos en `data/`. El análisis avanzado necesita, como mínimo:

- `results.csv`
- `races.csv`
- `drivers.csv`
- `constructors.csv`

## Ejecución

Desde la raíz del repositorio:

```bash
pip install -r requirements.txt
cd scripts
python analisis_avanzado.py
```

## Objetivo de aprendizaje

Este repositorio refleja una fase inicial de mi transición desde sistemas e integración hacia datos. Los siguientes pasos previstos son tipar el esquema de entrada, tratar calidad de datos de forma explícita y guardar salidas analíticas en formatos más adecuados para procesamiento, como Parquet.

## Otro proyecto relacionado

- [Analizador de Vueltas](https://github.com/ACapafons/AnalizadorVueltas): análisis de sesiones de clasificación y telemetría básica con Python.
