from LinearRegression import LinearRegression
from DecisionTree import DecisionTree

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/app/<a>', methods = ['POST'])
def returnClassify(a):
    testList = [i for i in a.split(",")]
    print testList
    lr = LinearRegression(testList).loadFiles()
    bin_dtree = DecisionTree(testList).loadFiles()

    return jsonify({"lr":str(lr), "bin":str(bin_dtree)})

if __name__ == '__main__':
    app.run(debug= True,port = 8000)