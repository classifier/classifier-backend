import os
import re
import sys
import pickle

from bottle import route, run, request, HTTPResponse

global sameModel


def get_words(text):
    f = list(re.sub(r'\W+', '', i) for i in text.lower().split(' '))
    return [i for i in f if i]


@route('/', method='POST')
def predict():
    postdata = request.body.read()
    print(postdata)
    query = get_words(postdata.decode('ascii'))
    print(query)
    prediction = sameModel.predict(hashingTF.transform(query))
    response = HTTPResponse(body=str(prediction), status=200)
    return response

os.environ['SPARK_HOME'] = '/Users/kerem/Documents/Repositories/Github/Classifier/classifier-backend/'
sys.path.append('/usr/local/bin/')


try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    print("Successfully imported Spark Modules")

    config = SparkConf().setMaster('local[*]').setAppName('SparkService')
    sc = SparkContext(conf=config)
    sc.setLogLevel("ERROR")

    from pyspark.mllib.feature import HashingTF
    from pyspark.mllib.classification import NaiveBayesModel
    hashingTF = HashingTF()

    my_path = os.path.dirname(os.path.abspath(__file__))

    sameModel = pickle.load(open(my_path + "/model.p", "rb"))

except ImportError as e:
    print("Can not import Spark Modules", e)
    sys.exit(1)


run(host='localhost', port=8001, debug=True)
