# Databricks notebook source
import pandas as pd
import plotly.express as px

table_name = 'filtered_table'
spark_data = spark.read.table(table_name)

df = spark_data.toPandas()
result1 = df.groupby(["country"])["finalWorth"].mean().reset_index()
fig = px.bar(result1, x="country", y="finalWorth")
fig.show()
