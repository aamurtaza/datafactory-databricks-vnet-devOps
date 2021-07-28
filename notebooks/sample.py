# Databricks notebook source
from pyspark.sql import *
import pandas as pd

sparkRDD = spark.sparkContext.textFile("/mnt/storage/sample.txt")

df = sparkRDD.map(lambda x: (x, )).toDF()

df.show()
