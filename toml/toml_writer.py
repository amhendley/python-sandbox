import json
# import rtoml
import toml


data = {
    'general':  {
        "title": "TOML Example",
        "dob": '1979-05-27T07:32:00-08:00',
    },
    'database': {
        'enabled': True,
        'ports': [
            8000,
            8001,
            8002
        ],
        'data': [
            ['delta', 'phi'],
            [3.14]
        ],
    },
    'database.temp_targets': {
        'cpu': 79.5,
        'case': 72.0
    },
    'servers': {},
    'servers.alpha': {
        'ip': "10.0.0.1",
        'role': "frontend"
    },
    'servers.beta': {
        'ip': "10.0.0.2",
        'role': "backend"
    }
}

toml_data = toml.dumps(data)
print(toml_data)

with open('/tmp/test.toml', mode='w') as file:
    toml.dump(toml_data, file)

with open('/tmp/test.toml', mode='r') as file:
    new_data = toml.load(file)
    print(toml.dumps(new_data))
