import requests

usr = {'nombre':'Alfonso',
    'email':'nada@nada.es',
    'pw_hash':'1234',
    'rol':'user',
    'f_alta':'2026-03-18'}


# resp = requests.post('http://127.0.0.1:5001/data/user',json=usr)
# print(resp)

resp = requests.get(
    'http://127.0.0.1:5001/data/user/by-email',
    params={'email':'uno@email.com'})

print(resp.content.decode("utf-8"))