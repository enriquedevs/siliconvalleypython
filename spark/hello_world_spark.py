
# To run successfully it needs pyspark from the spark version, in this case 2.3.3
# Install spark locally: https://medium.com/luckspark/installing-spark-2-3-0-on-macos-high-sierra-276a127b8b85
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('HelloWorldSpark')
sc = SparkContext(conf=conf)

rdd = sc.textFile('file:////Users/enrique/server/spark-2.3.3-bin-hadoop2.7/README.md')
print(rdd.count())
