import json


sample = {
    'album': 'Machine Head',
    'artist': 'Deep Purple',
    'year': '1971',
    'composer': 'Deep Purple'

}

required_keys = [
    'album',
    'artist',
    'year'
]

required_keys_2 = required_keys.copy()
required_keys_2.remove('year')

missing_keys = [
    'tracks'
]

# Using `all` to ensure all the required keys are present
assert all(k in sample for k in required_keys), 'Oops. We are missing something.'
# Using `any` to check that at a minimum we at least have one of the required keys
assert any(k in sample for k in required_keys_2), 'We might be missing something.'
# This test demonstrates when a required key is missing
assert all(k in sample for k in missing_keys), 'We are definitely missing something.'
