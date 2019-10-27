import requests
kv = {'key1':' values', 'key2': 'values'}
requests.post('http://localhost:8000/api/', json=kv)