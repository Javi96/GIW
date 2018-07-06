# -*- coding: utf-8 -*-
 
##
## INCLUIR LA CABECERA AQUI
## 

from pymongo import MongoClient
from bottle import run, get, template, request    

def create_tpl_agg1(data):
    count = 0
    text = """<!DOCTYPE html>
    <html lang="es">
    	<head>
    		<title>Result create_tpl_agg1</title>
            <charset="utf-8" />
        </head>"""
    text = text + '\n\t<body>'
    text = text + '\n\t\t' + '<h1>Query número 1</h1>'
    text = text + '\n\t\t' + '<table style="width:100%" border=1>'
    text = text + '\n\t\t\t<tr>'
    text = text + '\n\t\t\t\t<td><strong>Nombre del pais</strong></td>'
    text = text + '\n\t\t\t\t<td><strong>Número de usuarios</strong></td>'
    text = text + '\n\t\t\t</tr>'
    for line in data:
        count += 1
        text = text + '\n\t\t\t<tr>'
        text = text + '\n\t\t\t\t<td>' + list(line.values())[0] + '</td>'
        text = text + '\n\t\t\t\t<td>' + str(list(line.values())[1]) + '</td>'
        text = text + '\n\t\t\t</tr>'
    text = text + '\n\t\t' + '</table>'
    text = text + '\n\t</body>'
    text = text + '\n\t\t\t<h1><strong>Número de resultados: ' + str(count) + '</strong></h1>'
    text = text+ '</html>'
    
    try:
        with open('agg1.tpl', 'w', encoding='utf-8') as file:
            file.write(text)
    except:
        print('Error with files')
        raise IOError

def create_tpl_agg2(data):
    count = 0
    text = """<!DOCTYPE html>
    <html lang="es">
    	<head>
    		<title>Result create_tpl_agg2</title>
            <charset="utf-8"/>
        </head>"""
    text = text + '\n\t<body>'
    text = text + '\n\t\t' + '<h1>Query número 2</h1>'
    text = text + '\n\t\t' + '<table style="width:100%" border=1>'
    text = text + '\n\t\t\t<tr>'
    text = text + '\n\t\t\t\t<td><strong>Nombre del producto</strong></td>'
    text = text + '\n\t\t\t\t<td><strong>Unidades vendidas</strong></td>'
    text = text + '\n\t\t\t\t<td><strong>Precio unitario</strong></td>'
    text = text + '\n\t\t\t</tr>'
    for line in data:
        count += 1
        text = text + '\n\t\t\t<tr>'
        text = text + '\n\t\t\t\t<td>' + list(list(line.values())[0].values())[0] + '</td>'
        text = text + '\n\t\t\t\t<td>' + str(list(line.values())[1]) + '</td>'
        text = text + '\n\t\t\t\t<td>' + str(list(list(line.values())[0].values())[1]) + '</td>'
        text = text + '\n\t\t\t</tr>'
    text = text + '\n\t\t' + '</table>'
    text = text + '\n\t</body>'
    text = text + '\n\t\t\t<h1><strong>Número de resultados: ' + str(count) + '</strong></h1>'
    text = text+ '</html>'
    
    try:
        with open('agg2.tpl', 'w', encoding='utf-8') as file:
            file.write(text)
    except:
        print('Error with files')
        raise IOError

        
def create_tpl_agg3(data):
    count = 0
    text = """<!DOCTYPE html>
    <html lang="es">
    	<head>
    		<title>Result create_tpl_agg3</title>
            <charset="utf-8"/>
        </head>"""
    text = text + '\n\t<body>'
    text = text + '\n\t\t' + '<h1>Query número 3</h1>'
    text = text + '\n\t\t' + '<table style="width:100%" border=1>'
    text = text + '\n\t\t\t<tr>'
    text = text + '\n\t\t\t\t<td><strong>Nombre del país</strong></td>'
    text = text + '\n\t\t\t\t<td><strong>Rango de edades</strong></td>'
    text = text + '\n\t\t\t</tr>'
    for line in data:
        count += 1
        text = text + '\n\t\t\t<tr>'
        text = text + '\n\t\t\t\t<td>' + list(line.values())[0] + '</td>'
        text = text + '\n\t\t\t\t<td>' + str(list(line.values())[1]) + '</td>'
        text = text + '\n\t\t\t</tr>'
    text = text + '\n\t\t' + '</table>'
    text = text + '\n\t</body>'
    text = text + '\n\t\t\t<h1><strong>Número de resultados: ' + str(count) + '</strong></h1>'
    text = text+ '</html>'
    
    try:
        with open('agg3.tpl', 'w', encoding='utf-8') as file:
            file.write(text)
    except:
        print('Error with files')
        raise IOError
        
        
        
def create_tpl_agg4(data):
    count = 0
    text = """<!DOCTYPE html>
    <html lang="es">
    	<head>
    		<title>Result create_tpl_agg4</title>
            <charset="utf-8"/>
        </head>"""
    text = text + '\n\t<body>'
    text = text + '\n\t\t' + '<h1>Query número 4</h1>'
    text = text + '\n\t\t' + '<table style="width:100%" border=1>'
    text = text + '\n\t\t\t<tr>'
    text = text + '\n\t\t\t\t<td><strong>Nombre del país</strong></td>'
    text = text + '\n\t\t\t\t<td><strong>Media de pedidos</strong></td>'
    text = text + '\n\t\t\t</tr>'
    for line in data:
        count += 1
        text = text + '\n\t\t\t<tr>'
        text = text + '\n\t\t\t\t<td>' + list(line.values())[0] + '</td>'
        text = text + '\n\t\t\t\t<td>' + str(list(line.values())[1]) + '</td>'
        text = text + '\n\t\t\t</tr>'
    text = text + '\n\t\t' + '</table>'
    text = text + '\n\t</body>'
    text = text + '\n\t\t\t<h1><strong>Número de resultados: ' + str(count) + '</strong></h1>'
    text = text+ '</html>'
    
    try:
        with open('agg4.tpl', 'w', encoding='utf-8') as file:
            file.write(text)
    except:
        print('Error with files')
        raise IOError


def create_tpl_agg5(data):
    count = 0
    text = """<!DOCTYPE html>
    <html lang="es">
    	<head>
    		<title>Result create_tpl_agg5</title>
            <charset="utf-8"/>
        </head>"""
    text = text + '\n\t<body>'
    text = text + '\n\t\t' + '<h1>Query número 5</h1>'
    text = text + '\n\t\t' + '<table style="width:100%" border=1>'
    text = text + '\n\t\t\t<tr>'
    text = text + '\n\t\t\t\t<td><strong>Nombre del país</strong></td>'
    text = text + '\n\t\t\t\t<td><strong>Total de euros gastados</strong></td>'
    text = text + '\n\t\t\t</tr>'
    for line in data:
        count += 1
        text = text + '\n\t\t\t<tr>'
        text = text + '\n\t\t\t\t<td>' + list(line.values())[0][0] + '</td>'
        text = text + '\n\t\t\t\t<td>' + str(list(line.values())[1]) + '</td>'
        text = text + '\n\t\t\t</tr>'
    text = text + '\n\t\t' + '</table>'
    text = text + '\n\t</body>'
    text = text + '\n\t\t\t<h1><strong>Número de resultados: ' + str(count) + '</strong></h1>'
    text = text+ '</html>'
    
    try:
        with open('agg5.tpl', 'w', encoding='utf-8') as file:
            file.write(text)
    except:
        print('Error with files')
        raise IOError

def create_tpl_2_columns(title, column1, column2, data):
    count = 0
    text = """<!DOCTYPE html>
    <html lang="es">
    	<head>
    		<title>""" + title + """</title>
            <charset="utf-8"/>
        </head>"""
    text = text + '\n\t<body>'
    text = text + '\n\t\t' + '<h1>' + title + '</h1>'
    text = text + '\n\t\t' + '<table style="width:100%" border=1>'
    text = text + '\n\t\t\t<tr>'
    text = text + '\n\t\t\t\t<td><strong>' + column1 + '</strong></td>'
    text = text + '\n\t\t\t\t<td><strong>' + column2 + '</strong></td>'
    text = text + '\n\t\t\t</tr>'
    for line in data:
        count += 1
        text = text + '\n\t\t\t<tr>'
        text = text + '\n\t\t\t\t<td>' + list(line.values())[0][0] + '</td>'
        text = text + '\n\t\t\t\t<td>' + str(list(line.values())[1]) + '</td>'
        text = text + '\n\t\t\t</tr>'
    text = text + '\n\t\t' + '</table>'
    text = text + '\n\t</body>'
    text = text + '\n\t\t\t<h1><strong>Número de resultados: ' + str(count) + '</strong></h1>'
    text = text+ '</html>'
    
    try:
        with open(title + '.tpl', 'w', encoding='utf-8') as file:
            file.write(text)
    except:
        print('Error with files')
        raise IOError

def create_tpl_3_columns(title, column1, column2, column3, data):
    count = 0
    text = """<!DOCTYPE html>
    <html lang="es">
    	<head>
    		<title>""" + title + """</title>
            <charset="utf-8"/>
        </head>"""
    text = text + '\n\t<body>'
    text = text + '\n\t\t' + '<h1>' + title + '</h1>'
    text = text + '\n\t\t' + '<table style="width:100%" border=1>'
    text = text + '\n\t\t\t<tr>'
    text = text + '\n\t\t\t\t<td><strong>' + column1 + '</strong></td>'
    text = text + '\n\t\t\t\t<td><strong>' + column2 + '</strong></td>'
    text = text + '\n\t\t\t\t<td><strong>' + column3 + '</strong></td>'
    text = text + '\n\t\t\t</tr>'
    for line in data:
        count += 1
        text = text + '\n\t\t\t<tr>'
        text = text + '\n\t\t\t\t<td>' + list(list(line.values())[0].values())[0] + '</td>'
        text = text + '\n\t\t\t\t<td>' + str(list(line.values())[1]) + '</td>'
        text = text + '\n\t\t\t\t<td>' + str(list(list(line.values())[0].values())[1]) + '</td>'
        text = text + '\n\t\t\t</tr>'
    text = text + '\n\t\t' + '</table>'
    text = text + '\n\t</body>'
    text = text + '\n\t\t\t<h1><strong>Número de resultados: ' + str(count) + '</strong></h1>'
    text = text+ '</html>'
    
    try:
        with open(title + '.tpl', 'w', encoding='utf-8') as file:
            file.write(text)
    except:
        print('Error with files')
        raise IOError

        
@get('/top_countries')
# http://localhost:8080/top_countries?n=3
def agg1():
    'FUNCIONA BIEN'
    """Recibe un parámetro n , y genera una página HTML mostrando los n paı́ses
    con más número de usuarios junto a dicho número de usuarios. En caso de
    empate a usuarios, los paı́ses se ordenan alfabéticamente. Lo resultados se deben
    mostrar en una tabla con 2 columnas: la primera contendrá el nombre del paı́s
    y la segunda el número de usuarios. Justo debajo de la tabla debe aparecer un
    mensaje indicando el número de resultados devueltos por esta consulta."""
  
    mongoclient = MongoClient()
    db = mongoclient['giw']
    usuarios = db['usuarios']
    try:
        n = int(request.query.n)
        if n <= 0: raise Exception
    except:
        return template('err.tpl')
    resultado = usuarios.aggregate([
            {'$project':{'pais':1, 'nombre':1}},
            {'$group':{'_id': '$pais', '_count':{'$sum':1}}},
            {'$sort':{'_count':-1, '_id':1}},
            {'$limit':n}            
    ])

    create_tpl_agg1(resultado)
    return template('agg1.tpl')


@get('/products')
# http://localhost:8080/products?min=2.34
def agg2():
    'FUNCIONA BIEN'
    """Recibe un parámetro min representando un precio mı́nimo. Genera una pági-
    na HTML que muestra, por cada producto cuyo precio es igual o superior a
    min , el número de unidades vendidas entre todos los pedidos junto con su pre-
    cio unitario (que será el mismo en todos los pedidos en los que aparezca). Los
    resultados se muestran en una tabla de 3 columnas: nombre de producto, núme-
    ro de unidades vendidas y finalmente precio unitario. Justo debajo de la tabla
    debe aparecer un mensaje indicando el número de resultados devueltos por esta
    consulta.
    """
    
    mongoclient = MongoClient()
    db = mongoclient['giw']
    pedidos = db['pedidos']
    try:
        pmin = float(request.query.min)
        if pmin <= 0: raise Exception
    except:
        return template('err.tpl')
    resultado = pedidos.aggregate([
            {'$project':{'_id':0,'lineas.nombre':1,'lineas.cantidad':1,'lineas.precio':1}},
            {'$unwind':'$lineas'},
            {'$match':{'lineas.precio':{'$gte':pmin}}},
            {'$group':{'_id':{'_nombre':'$lineas.nombre','_precio':'$lineas.precio'},'_unidades':{'$sum':'$lineas.cantidad'}}}
            ])
    
    create_tpl_agg2(resultado)
    return template('agg2.tpl')

    
@get('/age_range')
# http://localhost:8080/age_range?min=80
def agg3():
    'FUNCIONA BIEN'
    """Recibe un parámetro min representando un numero mı́nimo de usuarios.
    Genera una página HTML que muestra, por cada paı́s que tiene más de min
    usuarios, el rango de edades, es decir, la diferencia entre la edad máxima y la
    edad mı́nima. Estos resultados deben aparecer ordenados de mayor a menor
    rango de edades, y en caso de empate, de manera alfabética por el nombre del
    paı́s. Los resultados se muestran en una tabla de 2 columnas: nombre de paı́s y
    rango de edades. Bajo de la tabla debe aparecer un mensaje indicando el número
    de resultados devueltos por esta consulta.
    """
    mongoclient = MongoClient()
    db = mongoclient['giw']
    usuarios = db['usuarios']
    try:
        umin = int(request.query.min)
        if umin < 0: raise Exception
    except:
        return template('err.tpl')
    resultado = usuarios.aggregate([
                {'$project':{'pais':1,'nombre':1,'edad':1}},
                {'$group':{'_id':'$pais', '_count':{'$sum':1}, '_max':{'$max':'$edad'}, '_min':{'$min':'$edad'}}},
                {'$match':{'_count':{'$gt':umin}}},
                {'$project':{'_rango':{'$subtract':['$_max','$_min']}}},
                {'$sort':{'_rango':-1,'_id':1}}
            ])
        
    create_tpl_agg3(resultado)
    return template('agg3.tpl')
    
    
@get('/avg_lines')
# http://localhost:8080/avg_lines
def agg4():
    'FUNCIONA BIEN'
    """Genera una página HTML que muestra, por cada paı́s, el número prome-
    dio de lı́neas que tienen los pedidos realizados por usuarios de dicho paı́s. Los
    resultados se muestran en una tabla de 2 columnas: nombre de paı́s y número
    de lı́neas promedio de sus pedidos. Bajo de la tabla debe aparecer un mensaje
    indicando el número de resultados devueltos por esta consulta.
    """
    
    mongoclient = MongoClient()
    db = mongoclient['giw']
    pedidos = db['pedidos']
    resultado = pedidos.aggregate([
            {'$project':{'_id':0, 'lineas':1, 'cliente':1}},
            {'$group':{'_id':'$cliente', 'pedidos':{'$sum':1}}},
            {'$lookup':{'from':'usuarios',
                        'localField':'_id',
                        'foreignField':'_id',
                        'as':'join_result'}},
            {'$project':{'_id':0, 'pedidos':1, 'join_result.pais':1}},
            {'$unwind':'$join_result'},
            {'$group':{'_id':'$join_result.pais', 'avg':{'$avg':'$pedidos'}}}
            ])

    create_tpl_agg4(resultado)
    return template('agg4.tpl')
    
@get('/total_country')
# http://localhost:8080/total_country?c=Alemania
def agg5():
    'FUNCIONA BIEN'
    """Recibe como parámetro c el nombre de un paı́s, y calcula el total de euros
    gastado en todos los pedidos realizados por usuarios de dicho paı́s. Los resulta-
    dos se muestran en una tabla de 2 columnas: nombre de paı́s y total de euros
    gastados. Se debe mostrar el número de resultados devueltos por esta consulta
    bajo la tabla"""
              
    mongoclient = MongoClient()
    db = mongoclient['giw']
    pedidos = db['pedidos']
    country = request.query.c
    resultado = pedidos.aggregate([
            {'$project':{'_id':0, 'total':1, 'cliente':1}},
            {'$group':{'_id':'$cliente', 'precio':{'$sum':'$total'}}},
            {'$lookup':{'from':'usuarios',
                        'localField':'_id',
                        'foreignField':'_id',
                        'as':'join_result'}},
            {'$project':{'_id':0, 'precio':1, 'join_result.pais':1}},
            {'$match':{'join_result.pais':{'$eq':country}}},
            {'$group':{'_id':'$join_result.pais', 'total_gasto':{'$sum':'$precio'}}}
            ])
    create_tpl_agg5(resultado)
    return template('agg5.tpl') 
        
if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)
