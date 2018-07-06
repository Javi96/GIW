# -*- coding: utf-8 -*-

# GIW - CURSO 17/18 - PRACTICA 7 - GRUPO 6
# AITOR CAYON RUANO
# JOSÉ JAVIER CORTÉS TEJADA
# FERNANDO PÉREZ GUTIÉRREZ
# GABRIEL SELLÉS SALVÀ

"""
Aitor Cayón Ruano, José Javier Cortés Tejada, Fernando Pérez Gutiérrez, Gabriel Sellés Salvà declaramos que esta solución
es fruto exclusivamente de nuestro trabajo personal. No hemos sido
ayudados por ninguna otra persona ni hemos obtenido la solución de
fuentes externas, y tampoco hemos compartido nuestra solución con
nadie. Declaramos además que no hemos realizado de manera deshonesta
ninguna otra actividad que pueda mejorar nuestros resultados
ni perjudicar los resultados de los demás.
"""

from pymongo import MongoClient
from bottle import run, get, template, request

def make_table_three_columns(cursor, file_name):
    """Crea una tabla con 3 columnas para el segundo apartado
    
    Parametros de entrada:
        cursor --- datos a mostrar en la tabla
        file_name -- nombre del fichero donde se guardara la tabla
        
    Retorno:
        count --- numero de filas añadidas a la tabla
    """
    
    count = 0
    # Añadimos los nombres de las columnas a la tabla
    text = '\n\t\t\t<tr>\n'
    text = text + '\t\t\t\t<td><strong>Nombre</strong></td>\n'
    text = text + '\t\t\t\t<td><strong>Email</strong></td>\n'
    text = text + '\t\t\t\t<td><strong>Fecha de nacimiento</strong></td>\n'
    text = text + '\t\t\t</tr>\n'
    # Añadimos la id, el email y la fecha de nacimiento de cada usuario
    for value in cursor:
        text = text + '\n\t\t\t<tr>\n'
        text = text + '\t\t\t\t<td>' + list(value.values())[0] + '</td>\n'
        text = text + '\t\t\t\t<td>' + list(value.values())[1] + '</td>\n'
        text = text + '\t\t\t\t<td>' + list(value.values())[2] + '</td>\n'
        text = text + '\t\t\t</tr>\n'
        count += 1
    try:
        # Creamos el nuevo tlp para mostrar la tabla
        with open(file_name + '_first.tpl', 'r', encoding='utf-8') as first:
            with open('second.tpl', 'r', encoding='utf-8') as second:
                with open(file_name + '.tpl', 'w', encoding='utf-8') as file:
                    file.write(first.read())
                    file.write(text)
                    file.write(second.read())
    except:
        print('Error with files')
        raise IOError
    return count
        
def make_table_ten_columns(cursor, file_name):
    """Crea una tabla con 10 columnas para el resto de apartados
    
    Parametros de entrada:
        cursor --- datos a mostrar en la tabla
        file_name -- nombre del fichero donde se guardara la tabla
        
    Retorno:
        count --- numero de filas añadidas a la tabla
    """
    
    count = 0
    # Añadimos los nombres de las columnas a la tabla
    text = '\n\t\t\t<tr>\n'
    text = text + '\t\t\t\t<td><strong>Nombre de usuario</strong></td>\n'
    text = text + '\t\t\t\t<td><strong>Email</strong></td>\n'
    text = text + '\t\t\t\t<td><strong>Página web</strong></td>\n'
    text = text + '\t\t\t\t<td><strong>Tarjeta de crédito</strong></td>\n'
    text = text + '\t\t\t\t<td><strong>Hash contraseña</strong></td>\n'
    text = text + '\t\t\t\t<td><strong>Nombre</strong></td>\n'
    text = text + '\t\t\t\t<td><strong>Apellido</strong></td>\n'
    text = text + '\t\t\t\t<td><strong>Dirección</strong></td>\n'
    text = text + '\t\t\t\t<td><strong>Aficiones</strong></td>\n'
    text = text + '\t\t\t\t<td><strong>Fecha de nacimiento</strong></td>\n'
    text = text + '\t\t\t</tr>\n'    
    for value in cursor:
        # Añadimos los campos necesarios de cada usuario
        text = text + '\n\t\t\t<tr>\n'
        text = text + '\t\t\t\t<td>' + list(value.values())[0] + '</td>\n'
        text = text + '\t\t\t\t<td>' + list(value.values())[1] + '</td>\n'
        text = text + '\t\t\t\t<td>' + list(value.values())[2] + '</td>\n'
        text = text + '\t\t\t\t<td>' + list(list(value.values())[3].values())[1] + '-' + list(list(list(value.values())[3].values())[0].values())[0] + '/' + list(list(list(value.values())[3].values())[0].values())[1] + '</td>\n'
        text = text + '\t\t\t\t<td>' + list(value.values())[4] + '</td>\n'
        text = text + '\t\t\t\t<td>' + list(value.values())[5] + '</td>\n'
        text = text + '\t\t\t\t<td>' + list(value.values())[6] + '</td>\n'
        text = text + '\t\t\t\t<td>' + list(list(value.values())[7].values())[0] + '-' + list(list(value.values())[7].values())[1] + '-' + list(list(value.values())[7].values())[2] + '-' + list(list(value.values())[7].values())[3] + '</td>\n'
        text = text + '\t\t\t\t<td>'
        for i in  list(value.values())[8]:
            text = text + i + '\n'
        text = text + '</td>\n'
        text = text + '\t\t\t\t<td>' + list(value.values())[9] + '</td>\n'
        text = text + '\t\t\t</tr>\n'
        count += 1
    try:
        # Creamos el nuevo tlp para mostrar la tabla
        with open(file_name + '_first.tpl', 'r', encoding='utf-8') as first:
            with open('second.tpl', 'r', encoding='utf-8') as second:
                with open(file_name + '.tpl', 'w', encoding='utf-8') as file:
                    file.write(first.read())
                    file.write(text)
                    file.write(second.read())
    except:
        print('Error with files')
        raise IOError
    return count

# mongoimport --db giw --collection usuarios --file usuarios.json
@get('/find_users')
def find_users():
    """Busca usuarios en funcion de su nombre, apellidos y fecha de nacimiento
    """
    
    # http://localhost:8080/find_users?name=Luz
    # http://localhost:8080/find_users?name=Luz&surname=Romero
    # http://localhost:8080/find_users?name=Luz&&surname=Romero&birthdate=2006-08-14
    name = request.query.name
    surname = request.query.surname
    birthdate = request.query.birthdate
    
    print (name, surname, birthdate)
    
    dicc = dict(request.query)
    consulta={}
    
    
    for x in dicc:
        if x == "name":
            consulta["name"]= name
        elif x =="surname":
            consulta["surname"]= surname
        elif x=="birthdate":
            consulta["birthdate"]= birthdate
        else:
            return template('error.tpl', error=("La consulta no admite el parametro " + str(x)))
            
    collection = MongoClient('localhost',27017).giw.usuarios    
    
    cursor = collection.find(consulta)      
    
    count = make_table_ten_columns(cursor, "find_users_result")
    return template('find_users_result.tpl', usuarios = count, name=name, surname=surname, birthdate=birthdate)

@get('/find_email_birthdate')
def email_birthdate():
    """Busca usuarios que hayan nacido entre dos fechas
    """
    
    # http://localhost:8080/find_email_birthdate?from=1973-01-01&to=1990-12-31

    ini = request.query['from']
    fin = request.query['to']
    
    print (ini, fin)
    
    dicc = dict(request.query)
    consulta={}
    
    for x in dicc:
        if x == "from":
            consulta["from"]= ini
        elif x =="to":
            consulta["to"]= fin
        else:
            return template('error.tpl', error="Los parametros introducidos son incorrectos")
    
    collection = MongoClient('localhost',27017).giw.usuarios    
    
    query = dict({"birthdate": {"$gte": consulta["from"], "$lt": consulta["to"]}})
    
    cursor = collection.find(query, {"id":1, "email":1, "birthdate":1})

    count = make_table_three_columns(cursor, "email_birthdate_result")
    return template('email_birthdate_result.tpl', usuarios = count, fecha1 = ini, fecha2 = fin)

@get('/find_country_likes_limit_sorted')
def find_country_likes_limit_sorted():
    """Busca usuarios que viven en un país en concreto y que tienen una serie de aficiones especificas
    """
    
    # http://localhost:8080/find_country_likes_limit_sorted?country=Irlanda&likes=movies,animals&limit=4&ord=asc
    
    country = request.query.country
    likes = request.query.likes.split(",")
    limit = int(request.query.limit)
    orden = request.query.ord
    
    print (country, likes, limit, orden)
    
    dicc = dict(request.query)
    consulta={}
    
    for x in dicc:
        if x == "country":
            consulta["country"]= country
        elif x =="likes":
            consulta["likes"]= likes
        elif x == "limit" and limit > 0:
            consulta["limit"]= limit
        elif x =="ord" and orden in ["asc", "des"]:
            if orden == "asc":
                consulta["orden"]= 1
            else:
                consulta["orden"] = -1
        else:
            return template('error.tpl', error="Los parametros introducidos son incorrectos")
    
    collection = MongoClient('localhost',27017).giw.usuarios 
    
    query = dict({"address.country": consulta["country"], "likes": {"$all": consulta["likes"]}})
    
    cursor = collection.find(query).sort("birthdate", consulta["orden"]).limit(consulta["limit"])
    
    count = make_table_ten_columns(cursor, "find_country_likes_limit_sorted_result")
    return template('find_country_likes_limit_sorted_result.tpl', usuarios=count, limit=limit, country=country, orden=orden)
            

@get('/find_birth_month')
def find_birth_month():
    """Busca usuarios nacidos en un mes en concreto
    """
    
    # http://localhost:8080/find_birth_month?month=abril
    month = request.query.month
    
    parser = dict({"enero": "-01-", "febrero": "-02-", "marzo": "-03-", "abril": "-04-", "mayo": "-05-", "junio": "-06-", "julio": "-07-", "agosto": "-08-", "septiembre": "-09-", "octubre": "-10-", "noviembre": "-11-", "diciembre": "-12-"})
    
    print (month)
    
    dicc = dict(request.query)
    
    for x in dicc:
        if x == "month" and month in parser.keys():
            consulta = parser[month]
        else:
            return template('error.tpl', error="Los parametros introducidos son incorrectos")
    
    print (consulta)
        
    collection = MongoClient('localhost',27017).giw.usuarios 
    
    cursor = collection.find({"birthdate" : {"$regex": consulta}}).sort("birthdate", 1)
    
    count = make_table_ten_columns(cursor, "find_birth_month_result")
    return template('find_birth_month_result.tpl', usuarios = count, month=month)

@get('/find_likes_not_ending')
def find_likes_not_ending():
    """Busca usuarios que no tienen aficiones que acaben en con un sufijo concreto
    """
    
    # http://localhost:8080/find_likes_not_ending?ending=s
    
    ending = request.query.ending
    
    print (ending)
    
    dicc = dict(request.query)
    
    for x in dicc:
        if x == "ending":
            consulta = ".*"+ending.lower()
        else:
            return template('error.tpl', error="Los parametros introducidos son incorrectos")
    
    query = dict({"likes": {"$not": {"$elemMatch": {"$regex": consulta}}}})
        
    collection = MongoClient('localhost',27017).giw.usuarios 
    
    cursor = collection.find(query)

    count = make_table_ten_columns(cursor, "find_likes_not_ending_result")
    return template('find_likes_not_ending_result.tpl', usuarios=count, ending=ending)

@get('/find_leap_year')     
def find_leap_year():
    """Busca usuarios nacidos en años bisiestos cuya tarjeta de credito caduque en el año pasado por parametro
    """
    
    # http://localhost:8080/find_leap_year?exp=20
    exp = request.query.exp
    
    
    dicc = dict(request.query)
        
    for x in dicc:
        if x == "exp" and len(exp)==2:
            consulta = exp
        else:
            return template('error.tpl', error="Los parametros introducidos son incorrectos")
    
    bisiesto = """function() {
                        if ("birthdate" in this) {
                                let year = Number(this["birthdate"].substr(0, 4));
                                if (year%4==0 && (!(year%100==0) || (year%400==0)))
                                    return true;
                                else
                                    return false;
                        }
                        else return false
                }"""   
        
    collection = MongoClient('localhost',27017).giw.usuarios
    
    cursor = collection.find({"credit_card.expire.year":consulta, "$where": bisiesto})

    count = make_table_ten_columns(cursor, "find_leap_year_result")
    return template('find_leap_year_result.tpl', usuarios=count, exp=consulta)

###################################
# NO MODIFICAR LA LLAMADA INICIAL #
###################################
if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)
