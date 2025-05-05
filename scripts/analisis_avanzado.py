from pyspark.sql import SparkSession

# Inicializar Spark
spark = SparkSession.builder     .appName("F1 Data Analysis - Avanzado")     .getOrCreate()

# Cargar datos
results_df = spark.read.option("header", True).csv("../data/results.csv")
races_df = spark.read.option("header", True).csv("../data/races.csv")
drivers_df = spark.read.option("header", True).csv("../data/drivers.csv")
constructors_df = spark.read.option("header", True).csv("../data/constructors.csv")

# Joins para obtener dataset completo
full_df = results_df.join(races_df, "raceId")                     .join(drivers_df, "driverId")                     .join(constructors_df, "constructorId")

# Filtrar por temporada
season_df = full_df.filter(full_df["year"] == "2020")

# Ranking de pilotos por puntos
season_df.groupBy("forename", "surname")          .sum("points")          .orderBy("sum(points)", ascending=False)          .show(10)

# Carreras por constructor
season_df.groupBy("name").count().orderBy("count", ascending=False).show(10)

# Finalizar Spark
spark.stop()
