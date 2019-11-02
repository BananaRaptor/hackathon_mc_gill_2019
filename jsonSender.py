import json
import requests


def getData():

    var1 = 3
    min1 = 1
    max1 = 5
    var2 = 2
    min2 = 1
    max2 = 5
    res = 14
    jsonOut(var1, min1, max1, var2, min2, max2, res)


def jsonOut(value1, min1, max1, value2, min2, max2, res):
    jsonTest = json.dumps(
        ['data', {'variable1': (value1, min1, max1)}, {'variable2': (value2, min2, max2)}, {'got': res}])
    response = requests.get('http://wolflo.net:6650')
    print response
    requests.post('http://wolflo.net:6650', jsonTest)


if __name__ == '__main__':
    getData()
