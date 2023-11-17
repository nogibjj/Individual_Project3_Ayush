# Databricks notebook source
# MAGIC %sql
# MAGIC REFRESH TABLE my_table
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

table_name = 'my_table'  

spark_df = spark.read.table(table_name)
spark_df.show()

# COMMAND ----------

from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("FilteredTableCreation").getOrCreate()

# Define the table name
output_table_name = "filtered_table"

# Perform filtering on the Spark DataFrame with error handling
try:
    filtered_df = spark_df.filter(spark_df['age'] > 60)
except Exception as e:
    raise RuntimeError(f"Error occurred during DataFrame filtering: {str(e)}")

try:
    filtered_df = filtered_df.drop('rank')
except Exception as e:
    raise RuntimeError(f"Error occurred while dropping column 'rank': {str(e)}")


# Data validation - Check if the filtered DataFrame is not empty
if filtered_df.count() == 0:
    raise ValueError("The filtered DataFrame is empty after applying the filter.")

# Save the filtered DataFrame as a table with error handling
try:
    filtered_df.write.saveAsTable(output_table_name, format="csv", mode="overwrite")
    print(f"Successfully saved filtered DataFrame as '{output_table_name}' in CSV format.")
except Exception as e:
    raise RuntimeError(f"Failed to save filtered DataFrame as a table: {str(e)}")


