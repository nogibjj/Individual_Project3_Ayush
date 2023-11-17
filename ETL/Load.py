# Databricks notebook source
# MAGIC %sql
# MAGIC REFRESH TABLE filtered_table

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder.appName("DeltaTableConversion").getOrCreate()

# Define the table name
table_name = 'filtered_table'

# Read the table data into a Spark DataFrame with error handling
try:
    spark_data = spark.read.table(table_name)
except Exception as e:
    raise RuntimeError(f"Failed to read data from table '{table_name}': {str(e)}")

from pyspark.sql.functions import col

# Assuming 'df' is your DataFrame
spark_data = spark_data.withColumn("finalWorth", col("finalWorth").cast("long"))
spark_data = spark_data.withColumn("year", col("year").cast("long"))
spark_data = spark_data.withColumn("month", col("month").cast("long"))
spark_data = spark_data.withColumn("birthDate", col("birthDate").cast("string"))


# Data validation - Check if the loaded Spark DataFrame is not empty
if spark_data.count() == 0:
    raise ValueError(f"The loaded Spark DataFrame from table '{table_name}' is empty.")

# Resolve data type conflict - Cast 'age' column to DoubleType
resolved_spark_data = spark_data.withColumn("age", col("age").cast("double"))  # Cast 'age' column to DoubleType

# Save the resolved Spark DataFrame as a Delta table with error handling
delta_table_path = "/mnt/data/delta_tables/my_delta_table"
try:
    resolved_spark_data.write.format("delta").mode("overwrite").save(delta_table_path)
    print(f"Successfully saved resolved Spark DataFrame from table '{table_name}' as a Delta table at '{delta_table_path}' (overwritten existing).")
except Exception as e:
    raise RuntimeError(f"Failed to save resolved Spark DataFrame as a Delta table: {str(e)}")


