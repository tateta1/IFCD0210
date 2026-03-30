import requests

usr = {'nombre':'alejandro',
    'email':'alejandro@gmail..es',
    'pw_hash':'1234',
    'rol':'user',
    'f_alta':'2026-03-17'}


#resp = requests.post('http://127.0.0.1:5000/data/user',json=usr)
#print(resp)

#resp = requests.get(
    'http://127.0.0.1:5000/data/user/by-email',
    params={'email':'alejandro@gmail.es'})

#print(resp.content.decode("utf-8"))
"""
post={
    "titulo":"POST MODIFICADO",
    "contenido":"Hola Mundo",
    "id_autor":1,
    "estado":"borrador"

}
curl -X POST http://127.0.0.1:5000/data/post -H 'Content-Type: application/json' -d "{'titulo':'Prueba de post','contenido':'Hola Mundo','id_autor':1,'estado':'borrador'
}"

curl -X POST http://127.0.0.1:5000/data/post -d "{\"titulo\":\"Prueba de post\",\"contenido\":\"Hola Mundo\",\"id_autor\":1,\"estado\":\"borrador\"}"


curl -X POST -H "Content-Type: application/json" -d "{\"titulo\":\"Prueba de post\",\"contenido\":\"Hola Mundo\",\"id_autor\":1,\"estado\":\"borrador\"}" http://127.0.0.1:5001/data/post
"""
# Lo anterior no funciona en windows.
# Esto sí:
Invoke-RestMethod -Uri "http://127.0.0.1:5001/data/post" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"titulo":"Prueba de post","contenido":"Hola Mundo","id_autor":1,"estado":"borrador"}'

Invoke-RestMethod -Uri "http://127.0.0.1:5001/data/post/1" -Method PUT -Headers @{ "Content-Type" = "application/json" } -Body '{"titulo":"POST MODIFICADO","contenido":"Hola Mundo","id_autor":1,"estado":"borrador"}'