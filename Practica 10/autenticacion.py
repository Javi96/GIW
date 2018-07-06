# -*- coding: utf-8 -*-

#
# CABECERA AQUI
#


from pymongo import MongoClient
from bottle import run, get, template, request, post
import string
import random
#import para los algoritmos hash. Usaremos SHA224
import hashlib
#Para la biblioteca "onetimepass"
import onetimepass as op
#Import para codificar y decodificar en base32.
import base64


##############
# APARTADO 1 #
##############

# 
# Explicación detallada del mecanismo escogido para el almacenamiento de
# contraseñas, explicando razonadamente por qué es seguro
#

"""
(/signup)
"""
#Busca en la base de datos el usuario con nick "nickname".
#Si no existe ninguno, devuelve False.
def get_user(nickname):
    collection = MongoClient('localhost',27017).giw.users
    consult={}
    consult['nickname']=nickname
    cursor=collection.find(consult)
    if(cursor.count()==0):
        return False;
    return cursor[0]
    

"""Genera un string aleatorio de 10 caracteres. Lo usamos para "sazonar" la contraseña."""
"""Obtenido de https://www.lawebdelprogramador.com/codigo/Python/2669-Funcion-para-generar-valores-aleatorios.html"""
def generate_random_string():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

'''Aplica la función hash a un string dado'''
def apply_hash_function(password):
    #Documentación obtenida en : https://docs.python.org/2/library/hashlib.html
    #Es necesario codificar la contraseña antes de aplicar la función hash. Nosotros lo hemos codificado en UTF-8.
    return hashlib.sha224(password.encode('utf-8')).hexdigest() 

"""Dada la contraseña que introduce el usuario, devuelve lo que se almacenará en la base de datos. También
devuelve el string añadido (la sal) a la contraseña antes de aplicar la función hash."""
def generate_stored_password(password):
    ##generamos la "sal". Será un string aleatorio de tamaño 10.
    added_string=generate_random_string()
    password=password+added_string
    print(password)
    #Devolvemos como segundo parametro la sal añadida, para poder almacenarla en la base de datos.
    return apply_hash_function(password), added_string

def exists_in_db(nickname):
    #Si existe, devuelve el user. Por lo tanto, hay que ponerlo así.
    if(get_user(nickname)==False):
        return False
    else:
        return True
 
def insert_into_db(nickname, name, country, email,password):
    collection = MongoClient('localhost',27017).giw.users
    user={}
    user['nickname']=nickname
    user['name']=name
    user['country']=country
    user['email']=email
    #No almacenamos la contraseña tal y como la ha introducido el usuario, sino que le aplicamos una función de hash.
    #También almacenamos el string añadido a la contraseña antes de aplicar la función hash.
    user['password'], user['added_string']=generate_stored_password(password)
    collection.insert_one(user)

def signup_service(nickname,name, country,email,password1,password2):
    if(password1!=password2):
        return "Las contraseñas no coinciden"
    if(exists_in_db(nickname)):
        return "El alias de usuario ya existe"
    insert_into_db(nickname, name, country,email, password1)
    return "Bienvenido usuario " + name


@get('/signup')
def service1_calculate():
    return template("signup")

@post('/signup')
def signup():
    try:
        nickname= request.forms.get('nickname')
        name= request.forms.get('name')
        country= request.forms.get('country')
        email= request.forms.get('email')
        password1=request.forms.get('password')
        password2=request.forms.get('password2')
        result=signup_service(nickname,name,country,email,password1,password2)
    except Exception as e:
        result=str(e)
    finally:
        return template('result.tpl',msg=result)


"""
(/change_password)
"""

def update_password(nickname,new_password):
     password,added_string=generate_stored_password(new_password)
     collection = MongoClient('localhost',27017).giw.users   
    
     collection.update_one({'nickname': nickname}, {'$set': {'password': password}})
     collection.update_one({'nickname': nickname}, {'$set': {'added_string': added_string}})

#Devuelve true si existe un usuario con un cierto nick y la contraseña introducida es la suya.
#En caso contrario, devuelve false.
def check_password(nickname, old_password):
     user=get_user(nickname)
     if(user==False):
         return False
     old_password=old_password+user['added_string']
     if(apply_hash_function(old_password)==user['password']):
         return True
     else:
         return False
     
@get('/change_password')
def change_password_template():
    return template('change_pass')

@post('/change_password')
def change_password():
    nickname= request.forms.get('nickname')
    old= request.forms.get('old_password')
    if(not check_password(nickname,old)):
        result='Usuario o contrase~na incorrectos'
    else:
        new_password= request.forms.get('new_password')
        update_password(nickname,new_password)
        result='La constraseña del usuario '+nickname+ ' ha sido modificada.'
    return template('result.tpl',msg=result)

"""
(/login)
"""

@get('/login')
def login_template():
    return template('login')


@post('/login')
def login():
    nickname=request.forms.get('nickname')
    password=request.forms.get('password')
    if(not check_password(nickname,password)):
        result="Usuario o contrase~na incorrectos"
    else:
        user=get_user(nickname)
        result= "Bienvenido "+ user['name']
    return template('result.tpl',msg=result)


##############
# APARTADO 2 #
##############

# 
# Explicación detallada de cómo se genera la semilla aleatoria, cómo se construye
# la URL de registro en Google Authenticator y cómo se genera el código QR
#
    
def insert_into_db_totp(nickname,name,country,email,password,seed):
    collection = MongoClient('localhost',27017).giw.users
    user={}
    user['nickname']=nickname
    user['name']=name
    user['country']=country
    user['email']=email
    #No almacenamos la contraseña tal y como la ha introducido el usuario, sino que le aplicamos una función de hash.
    #También almacenamos el string añadido a la contraseña antes de aplicar la función hash.
    user['password'], user['added_string']=generate_stored_password(password)
    user['seed']=seed
    collection.insert_one(user)
    

def generate_base32_seed():
    """Genera una semilla en base 32 de tamaño 12"""
    #Array que contendrá todos los posibles elementos de la semilla.
    #Obtenidos de https://en.wikipedia.org/wiki/Base32
    possible=string.ascii_uppercase+ "234567"
    
    result=""
    for x in range(0,12):
        result=result+possible[random.randrange(32)]
        
    #Pasamos el string a bytes.
    result=bytes(result,'utf-8')
    r= base64.b32encode(result) 
    #Lo volvemos a pasar a string para que se almacene el na DB.
    return r.decode('utf-8')


def signup_service_totp(nickname,name, country,email,password1,password2):
    if(password1!=password2):
        return "Las contraseñas no coinciden"
    if(exists_in_db(nickname)):
        return "El alias de usuario ya existe"
    seed=generate_base32_seed()
    insert_into_db_totp(nickname, name, country,email, password1,seed)
    
    return template('qrsite.tpl',link="http://api.qrserver.com/v1/create-qr-code/?data=otpauth://totp/MyGIWAuthenticationApp:"+email+"?secret="+seed+"&issuer=MyGIWAuthenticationApp&size=250x250", seed=seed, email=email)

@get('/signup_totp')
def signup_totp_template():
    return template('signup_totp')

@post('/signup_totp')
def signup_totp():
    try:
        nickname= request.forms.get('nickname')
        name= request.forms.get('name')
        country= request.forms.get('country')
        email= request.forms.get('email')
        password1=request.forms.get('password')
        password2=request.forms.get('password2')
        return signup_service_totp(nickname,name,country,email,password1,password2)
    except Exception as e:
        result=str(e)
        return template('result.tpl',msg=result) 

@get('/login_totp')
def login_totp_template():
    return template('login_totp')

@post('/login_totp')        
def login_totp():
    nickname= request.forms.get('nickname')
    password= request.forms.get('password')
    totp= request.forms.get('totp')
    
    #Comprobamos que el usuario exista y que la contraseña introducida sea la correcta.
    user=get_user(nickname)
    if(not check_password(nickname, password) or not op.valid_totp(token=totp, secret=user['seed'])):
        result="Usuario o contrase~na incorrectos"
    else:
        user=get_user(nickname)
        result="Bienvenido "+user['name']
    return template('result.tpl',msg=result)    
    

if __name__ == "__main__":
    # NO MODIFICAR LOS PARÁMETROS DE run()
    run(host='localhost',port=8080,debug=True)
