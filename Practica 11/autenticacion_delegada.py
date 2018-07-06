# -*- coding: utf-8 -*-

#
# CABECERA AQUI
#

#Biblioteca para tratar peticiones HTTP.
#http://docs.python-requests.org/en/master/
import requests

from bottle import run, get, template, request
# Resto de importaciones


# Credenciales. 
# https://developers.google.com/identity/protocols/OpenIDConnect#appsetup
# Copiar los valores adecuados.

#INTRODUCIDOS POR MI

CLIENT_ID     = "787716095146-nb2dgiqkjquclq018bv47fqllcmkoi7q.apps.googleusercontent.com"
CLIENT_SECRET = "6exWBDOImEXi22fe1foNHemD"
REDIRECT_URI  = "http://localhost:8080/token"


# Fichero de descubrimiento para obtener el 'authorization endpoint' y el 
# 'token endpoint'
# https://developers.google.com/identity/protocols/OpenIDConnect#authenticatingtheuser
DISCOVERY_DOC = "https://accounts.google.com/.well-known/openid-configuration"

#AÑADIDO POR MI
CONFIGURATION_JSON=requests.get(DISCOVERY_DOC).json()

# Token validation endpoint para decodificar JWT
# https://developers.google.com/identity/protocols/OpenIDConnect#validatinganidtoken
TOKENINFO_ENDPOINT = 'https://www.googleapis.com/oauth2/v3/tokeninfo'

state=""

@get('/login_google')
def login_google():
    
    state="1111"
    
    authorization_endpoint=CONFIGURATION_JSON['authorization_endpoint']
    text=authorization_endpoint+'?client_id='+CLIENT_ID+'&response_type=code&scope=openid%20email&redirect_uri='+REDIRECT_URI
    #Tenemos la pagina web
    return template('initial.tpl',text=text, STATE=state)


@get('/token')
def token():
    #Se devuelve un código temporal en code.
    #https://bottlepy.org/docs/dev/api.html
    print(request.text())
    code=request.params.get('code')
    #Realizamos la petición para obtener el id_token y el access token.
    r=requests.post(CONFIGURATION_JSON['token_endpoint'], data={'code':code, 'client_secret':CLIENT_SECRET, 'client_id':CLIENT_ID, 'redirect_uri':REDIRECT_URI, 'grant_type':'authorization_code'});    
    id_token=r.json()['id_token']
    #Ahora tenemos el id_token.
    #Hagamos la petición remota para obtener el mail del user.
    r=requests.post(TOKENINFO_ENDPOINT, data={'id_token':id_token})
    #https://www.googleapis.com/oauth2/v3/tokeninfo
    print(r)
    r=r.json()    
    return template('result.tpl', text="Bienvenido "+r['email'])
  

if __name__ == "__main__":
    # NO MODIFICAR LOS PARÁMETROS DE run()
    run(host='localhost',port=8080,debug=True)
