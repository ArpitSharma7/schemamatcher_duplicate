from schemamatcher_spark_dup.defaults import *
from pyspark.sql import SparkSession
import pandas as pd


def count_length(col_string):
    return len(col_string)


def get_count(df_part, col_list):
    df = pd.DataFrame(df_part, columns=col_list)
    if len(df) == 0:
        return df.values.tolist()
    df['column_count'] = df['column'].apply(lambda z: count_length(z))
    return df.values.tolist()


def column_count(df):
    columns = df.columns
    df_rdd = df.rdd.mapPartitions(lambda x: get_count(x, columns))

    spark = SparkSession.builder.getOrCreate()
    df = spark.createDataFrame(df_rdd, SCHEMA)
    return df


def main():  # pragma: no cover
    spark = SparkSession.builder.getOrCreate()

    df = spark.createDataFrame(
        [
            (1, 'Stocks'),
            (2, 'Price')
        ],
        ['id', 'column']
    )
    df = df.repartition(PART_BY, 'id')

    df = column_count(df)
    df.show()


