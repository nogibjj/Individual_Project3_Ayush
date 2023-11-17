[![CI](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject03/actions/workflows/01_Install.yml/badge.svg)](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject03/actions/workflows/01_Install.yml)

# Databricks ETL (Extract Transform Load) Pipeline

## Purpose :
The purpose of this project is to perform ETL operations with a pipeline on Databricks using Spqrk SQL. 

# Components:

## 1 - Databricks notebooks for ETL

Azure Workspace [Link](https://adb-2312128046693227.7.azuredatabricks.net/browse/folders/2979888917193756?o=2312128046693227)

What is a Data Pipeline? 
Data pipeline is a workflow that defines the movement and transformation of data from its raw form to a desired output, incorporating various operations like data ingestion, cleansing, transformation, analysis, and model training or deployment.

File Name - an Azure Databricks workspace that extracts data, performs transformations, and loads the data into a final output using Pyspark. 
 * Creates a Spark Session `spark`
 * *Extract* - Extracts data from `forbes_2022_billionaires.csv` in the Data Folder, and stores it in a Dataframe `spark_df`
 * *Transform* - Creates a Spark DataFrame called `filtered_df` from the 'spark_df' dataframe, subsetting the rows with age > 60 and dropping the first column. 
 * *Load* - Saves the transformed spark Dataframe as a Delta table called `my_delta_table`

Ingestion :
![ETL Operations](https://github.com/nogibjj/Individual_Project3_Ayush/blob/main/Images/ingestion.png)

Transform : 
![ETL Operations](https://github.com/nogibjj/Individual_Project3_Ayush/blob/main/Images/transform.png)

Load : 
![ETL Operations](https://github.com/nogibjj/Individual_Project3_Ayush/blob/main/Images/Load.png)

## 2 - Usage of Spark SQL for data transformations

#### Scale and Distribution:
SparkSQL excels in processing massive datasets distributed across clusters, unlike MySQL, which operates on a single server.

#### Complex Analytics and Processing:
SparkSQL seamlessly handles complex analytics, machine learning pipelines, graph processing, and real-time data streaming, areas where MySQL lacks capabilities.

#### Data Variety and Integration:
SparkSQL effortlessly manages data from diverse sources (HDFS, Parquet, JSON, etc.), while MySQL primarily handles structured relational data.

#### Scalability and Performance:
SparkSQL scales horizontally by distributing tasks across nodes, unlike MySQL, which typically scales vertically (upgrading hardware).
SparkSQL’s in-memory processing boosts performance for iterative algorithms and ad-hoc queries on large datasets.

#### Real-Time Analytics and Queries:
SparkSQL offers faster real-time analytics and interactive querying due to caching and optimized distributed processing, outperforming MySQL in many cases.

In summary, SparkSQL is preferred over MySQL when dealing with massive distributed datasets, complex analytics, diverse data sources, scalability needs, and real-time analytics or queries.

File Name - `03_Spark_SQL_For_DataTransformation.py` - an Azure Databricks Notebook that queries the 2022_billionaire Delta Table created above using *Spark SQL*

 * Create a Spark Session using PySpark.SQL
 * Query the `delta_table` table created in the above step (#2)
 * Using the *GROUP BY* command in SQL to transform the data and make it readable
 * Writing this data into a new delta table for future steps (visualization)
 * Error handling at every step
![Usage of Spark SQL](https://github.com/nogibjj/Individual_Project3_Ayush/blob/main/Images/Pyspark%20Transformation%20and%20Error%20handling.png)

## 3 - Proper error handling and data validation
Error handling and Data Validation is performed individually in every code and notebook. Errors are published wherever possible, and empty dataframes are flagged as well.

## 4 - Usage of Delta Lake for data storage

File Name - `02_Delta_Lake_For_Storage.py` - an Azure Databricks Notebook that creates a Delta Table in the Delta Lake using *Spark*

 * Read the 2022_billionaire dataset from the Data Folder
 * Create a pandas DataFrame `data`
 * Convert the Pandas DataFrame to a Spark Dataframe `spark_df` (because only spark dataframes can be converted to a delta format)
 * Save the Spark DataFrame as a Delta-Table `delta_table` (Overwrite mode is on so that if the table already exists, it will be re-written instead of giving errors)
 * Error handling at every step to highlight errors
![Delta Lake for Storage](https://github.com/nogibjj/Individual_Project3_Ayush/blob/main/Images/DeltaLakeStorage.png)

## 5 - Visualization of the transformed data

File Name - `04_Visualization_of_Transformed_Data.py` - an Azure Databricks Notebook that creates a Visualization based on the *transformed* delta table created in Step 03

 * Query the `forbes_2022_billionaires` Delta Table usign Spark SQL
 * Generate a chart of the data using Matplotlib and plotly.
 * Save the chart as `net_worth.png` in the Azure workspace
![Visualization](https://github.com/nogibjj/Individual_Project3_Ayush/blob/main/Images/Visualization.png)

## 6 - An automated trigger to initiate the pipeline

The pipeline has been set up to run automatically each day at 04:10:00.

#### Workflow Pipeline : The workflow first creates the table, then Transforms and Loads the Data, and then creates a Visualization for it using codes from steps 2, 3, and 5 from above 
![Workflow Chart](https://github.com/nogibjj/Individual_Project3_Ayush/blob/main/Images/workflow_pipeline.png)

#### Workflow Successful Run
![Workflow Run](https://github.com/nogibjj/Individual_Project3_Ayush/blob/main/Images/Workflow.png)

## 7 - Video Demo - [Link]()









#
## File Index

Files in this repository include:


## 1. Readme
  The `README.md` file is a markdown file that contains basic information about the repository, what files it contains, and how to consume them


## 2. Requirements
  The `requirements.txt` file has a list of packages to be installed for any required project. Currently, my requirements file contains some basic python packages.


## 3. Codes
  This folder contains all the code files used in this repository - the files named "Test_" will be used for testing and the remaining will define certain functions


## 4. Resources
  -  This folder contains any other files relevant to this project. Currently, I have added -


## 5. CI/CD Automation Files


  ### 5(a). Makefile
  The `Makefile` contains instructions for installing packages (specified in `requirements.txt`), formatting the code (using black formatting), testing the code (running all the sample python code files starting with the term *'Check...'* ), and linting the code using pylint


  ### 5(b). Github Actions
  Github Actions uses the `main.yml` file to call the functions defined in the Makefile based on triggers such as push or pull. Currently, every time a change is pushed onto the repository, it runs the install packages, formatting the code, linting the code, and then testing the code functions


  ### 5(c). Devcontainer
  
  The `.devcontainer` folder mainly contains two files - 
  * `Dockerfile` defines the environment variables - essentially it ensures that all collaborators using the repository are working on the same environment to avoid conflicts and version mismatch issues
  * `devcontainer.json` is a json file that specifies the environment variables including the installed extensions in the virtual environment
