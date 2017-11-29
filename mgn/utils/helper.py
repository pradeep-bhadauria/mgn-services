from flask import json


class Helper:

    @staticmethod
    def json_list(data):
        result = [i.serialize for i in data.all()]
        return json.dumps(result)
