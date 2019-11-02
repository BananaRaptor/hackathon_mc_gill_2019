import json
import requests

var1 = 1
var2 = 2
exp = 3
res = 14


def jsonOut():
    jsonTest = json.dumps(['data', {'input': (var1, var2)}, {'expected': exp}, {'got': res}])
    response = requests.get('http://wolflo.net:6650')
    requests.post('http://wolflo.net:6650', jsonTest)
    print response
if __name__ == '__main__':
    jsonOut()







