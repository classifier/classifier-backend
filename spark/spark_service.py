import os
import sys

os.environ['SPARK_HOME'] = 'spark/spark'
sys.path.append('spark/spark/python/')


try:
   from pyspark import SparkContext
   from pyspark import SparkConf
   print("Successfully imported Spark Modules")

except ImportError as e:
   print("Can not import Spark Modules", e)
   sys.exit(1)


config = SparkConf().setMaster('local[*]').setAppName('SparkService')
sc = SparkContext(conf=config)
sc.setLogLevel("ERROR")


from pyspark.mllib.feature import HashingTF
from pyspark.mllib.classification import NaiveBayesModel

hashingTF = HashingTF()

sameModel = NaiveBayesModel.load(sc, "spark/nbm")

print(sameModel.predict(hashingTF.transform("This is good place".split(" "))))

