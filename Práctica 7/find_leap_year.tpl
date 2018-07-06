<!--
	# GIW - CURSO 17/18 - PRACTICA 7 - GRUPO 6
	# AITOR CAYON RUANO
	# JOSÉ JAVIER CORTÉS TEJADA
	# FERNANDO PÉREZ GUTIÉREZ
	# GABRIEL SELLÉS SALVÀ
-->
<!--
	Aitor Cayón Ruano, José Javier Cortés Tejada, Fernando Pérez Gutiérrez, Gabriel Sellés Salvà declaramos que esta solución
	es fruto exclusivamente de nuestro trabajo personal. No hemos sido
	ayudados por ninguna otra persona ni hemos obtenido la solución de
	fuentes externas, y tampoco hemos compartido nuestra solución con
	nadie. Declaramos además que no hemos realizado de manera deshonesta
	ninguna otra actividad que pueda mejorar nuestros resultados
	ni perjudicar los resultados de los demás.
-->

<!DOCTYPE html>
<html lang="es">
	<head>
		<title>Practica 7</title>
		<meta charset="utf-8" />
	</head>
	<body>
		<h1>Practica 7 GIW</h1>
		<h2>Buscar fecha de caducidad de tarjeta y nacimiento en ano bisiesto (Fecha de Caducidad): </h2>	
	
		<form action="/find_users" method="get">
			<h2>Fecha de caducidad: {{exp}}</h2>
			%for document in cursor:
				Document: {{document}}
			%end	
		</form>		
	</body>
</html>
