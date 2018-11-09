# Python3

import json

def buildCommand(jsonFile):
    DEFAULT_VALUE_TABLE = {int: 0, float: 0, list: [], str: ''}
    def getDefaultObj(obj):
        for k, v in obj.items():
            typ = type(v)
            obj[k] = DEFAULT_VALUE_TABLE[typ] if typ in DEFAULT_VALUE_TABLE else getDefaultObj(v)
        return obj

    return json.dumps(getDefaultObj(json.loads(jsonFile)))
