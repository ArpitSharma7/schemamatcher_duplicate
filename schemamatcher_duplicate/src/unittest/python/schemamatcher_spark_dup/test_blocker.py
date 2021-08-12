from schemamatcher_spark_dup.blocker import *
from schemamatcher_spark_dup.defaults import *
from pyspark.sql import SparkSession
import os
import shutil


class TestBlocker:

    def prepare(self):
        spark = SparkSession.builder.master('local[*]').appName("blocker").getOrCreate()
        # if not os.path.isfile('schemamatcher_spark_dup.zip'):
        #     current_path = os.getcwd() + '/src/main/python/schemamatcher_spark_dup'
        #     shutil.make_archive('schemamatcher_spark_dup', 'zip', current_path)
        spark.sparkContext.addPyFile('/Users/arsharma/schemamatcher_duplicate/schemamatcher_spark_dup.zip')

        self.df = spark.createDataFrame(
            [
                (1, 'Stocks'),
                (2, 'Price')
            ],
            ['id', 'column']
        )

    def test_count_length(self):
        s1 = ""
        assert count_length(s1) == 0
        s2 = "test_hello"
        assert count_length(s2) == 10

    def test_get_count(self):
        self.prepare()
        columns = self.df.columns
        df_rdd_list = self.df.rdd.collect()
        temp = get_count(df_rdd_list, columns)
        assert temp == [[1, 'Stocks', 6], [2, 'Price', 5]]

    def test_column_count(self):
        self.prepare()
        df = column_count(self.df)
        assert df.count() == 2
