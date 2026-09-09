# ==============================
# 1. Importar librerías necesarias
# ==============================
import urllib.request
import json

print("\n")  # Espacio visual


# ==============================
# 2. Crear la petición HTTP con cabeceras
# ==============================
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/api/personas.json',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/35.0.1916.47 Safari/537.36'
    }
)

print("\n")  # Espacio visual


# ==============================
# 3. Obtener la respuesta del servidor
# ==============================
respuesta = urllib.request.urlopen(peticion)
print(respuesta)

cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)

print("\n")  # Espacio visual


# ==============================
# 4. Procesar la respuesta JSON
# ==============================
json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))
print(json_respuesta)

print("\n")  # Espacio visual


# ==============================
# 5. Imprimir nombres y edades
# ==============================
print('Nombres de las personas en el archivo JSON :')
for persona in json_respuesta['personas']:
    print(persona['nombre'], persona['edad'])

print("\n")  # Espacio visual


# ==============================
# 6. Acceder a otros datos del JSON
# ==============================
print(f'Total de personas: {json_respuesta["total"]}')
print(f'Mensaje: {json_respuesta["mensaje"]}')
