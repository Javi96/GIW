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
		<title>Result find_users</title>
		<meta charset="utf-8" />
	</head>
	<body>

 		<h1>Numero de usuarios: {{usuarios}}</h1>
		<h2>Usuarios con nombre: {{name}} , apellido: {{surname}} y fecha de nacimiento: {{birthdate}}</h2>
		<table style="width:100%" border=1>
			<tr>
				<td><strong>Nombre de usuario</strong></td>
				<td><strong>Email</strong></td>
				<td><strong>Página web</strong></td>
				<td><strong>Tarjeta de crédito</strong></td>
				<td><strong>Hash contraseña</strong></td>
				<td><strong>Nombre</strong></td>
				<td><strong>Apellido</strong></td>
				<td><strong>Dirección</strong></td>
				<td><strong>Aficiones</strong></td>
				<td><strong>Fecha de nacimiento</strong></td>
			</tr>

			<tr>
				<td>burgoscarla</td>
				<td>robertocastell@yahoo.com</td>
				<td>http://carrasco-amor.net/search/homepage.htm</td>
				<td>3337334668340921-23/02</td>
				<td>3c7b1d1b712258774081e3d018a431b274fbfb14</td>
				<td>Luz</td>
				<td>Romero</td>
				<td>Serbia-35214-Cuesta Gregorio Martínez-305</td>
				<td>baseball
animals
dancing
painting
</td>
				<td>2006-08-14</td>
			</tr>
		</table>
		<h2><a href= "http://localhost:8080/"> Volver a la pagina inicial</a></h2>
	</body>
</html>