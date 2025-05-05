from pyspark.sql import SparkSession

# Inicializar Spark
spark = SparkSession.builder     .appName("F1 Data Analysis - Inicial")     .getOrCreate()

# Cargar resultados
df = spark.read.option("header", True).csv("../data/results.csv")

# Mostrar esquema y primeros registros
df.printSchema()
df.show(10)

# Agrupar por constructorId
df.groupBy("constructorId").count().show()

# Finalizar Spark
spark.stop()
