import json
from jsonschema import validate, draft7_format_checker

# Describe what kind of json you expect.
config = [
    {
        "id": "a7776b04-785d-4023-a4de-25815152c894",
        "schema": {
            "type" : "object",
            "properties" : {
                "description" : {"type" : "string"},
                "status" : {"type" : "boolean"},
                "value_a" : {"type" : "number"},
                "value_b" : {"type" : "string", "pattern": "^([0-9]\.[0-9]{3})$"},
                "timestamp": {"type": "string", "format": "date-time"},
                "email": {"type": "string", "format": "email"},
                "account": {"$ref": "#/definitions/account"}
            },
            "required": [
                "timestamp"
            ]
        }
    }
]

# Convert json to python object.
my_json = {
    "description": "Hello world!",
    "status": True,
    "value_a": 1,
    "value_b": "3.143",
    "timestamp": "2020-03-18T21:03:20+10:00",
    "email": "reply me@email.com",
    "account": {
        "bsb": "123-456",
        "accountName": "Mr Andrew Hendley",
        "accountNumber": "343274327422"
    }
}

# Convert json to python object.
my_json = {
    "description": "Hello world!",
    "status": True,
    "value_a": 1,
    "value_b": "3.143",
    "timestamp": "2020-03-18T21:03:20+10:00",
    "email": "reply me@email.com",
    "account": {
        "bsb": "123-456",
        "accountName": "Mr Andrew Hendley",
        "accountNumber": "343274327422"
    }
}

# Validate will raise exception if given json is not
# what is described in schema.
schema = config[0]['schema']

validate(instance=my_json, schema=schema, format_checker=draft7_format_checker)

# print for debug
print(json.dumps(my_json, indent=2))