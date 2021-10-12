#!/usr/bin/env python3
"""
Requirements
* pyjwt
* cryptography
"""
import os
import datetime
import uuid
import jwt

use_config = 'DEV'
shift_nbf = True
shift_nbf_minutes = 1
configurations = {
    'DEV': {
        'kid': str(uuid.uuid4()),
        'private_key': f'{os.environ["HOME"]}/.ssh/id_rsa',
        'audience': 'me.com',
        'subject': 'JWT Generator',
        'issuer': 'ACME',
        'duration': 1,
        'extra_payload': {
            'user': 'john.doe',
            'role': 'sales'
        }
    },
    'TEST': {
        'kid': str(uuid.uuid4()),
        'private_key': f'{os.environ["HOME"]}/.ssh/id_rsa',
        'audience': 'me.com',
        'subject': 'JWT Generator',
        'issuer': 'ACME',
        'duration': 1
    }
}

private_key_path = configurations[use_config]['private_key']

with open(private_key_path) as file:
    private_key = ''.join(file.readlines())

jwt_kid = configurations[use_config]['kid']
jwt_algorithm = 'RS256'

jwt_headers = {
    'kid': jwt_kid,
    'alg': jwt_algorithm
}

jwt_audience = configurations[use_config]['audience']
jwt_subject = configurations[use_config]['subject']
jwt_issuer = configurations[use_config]['issuer']
jwt_id = str(uuid.uuid4())
jwt_timestamp = datetime.datetime.now()
if shift_nbf:
    jwt_timestamp += datetime.timedelta(minutes=shift_nbf_minutes)
jwt_expiry = (jwt_timestamp + datetime.timedelta(
    days=int(configurations[use_config]['duration'])))

jwt_payload = {
    'jti': jwt_id,
    'sub': jwt_subject,
    'aud': jwt_audience,
    'iss': jwt_issuer,
    'exp': int(jwt_expiry.timestamp()),
    'nbf': int(jwt_timestamp.timestamp())
}

if 'extra_payload' in configurations[use_config]:
    for k, v in configurations[use_config]['extra_payload'].items():
        jwt_payload[k] = v

print('Create JWT Token')
print(f'  Configuration: {use_config}')
print(f'  Headers: {jwt_headers}')
print(f'  Payload: {jwt_payload}')
print()

jwt_token = jwt.encode(
    payload=jwt_payload,
    key=private_key,
    algorithm=jwt_algorithm,
    headers=jwt_headers
)

print(f'Token:\n{jwt_token}')
