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
		<title>Result find_country_likes_limit_sorted</title>
		<meta charset="utf-8" />
	</head>
	<body>

		<h1>Numero de usuarios: {{usuarios}}</h1>
 		<h2>{{limit}} primeros usuarios de {{country}} con los gustos indicados. Ordenados por fecha de nacimiento {{orden}}:</h2>
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
				<td>grauroberto</td>
				<td>lmontenegro@gmail.com</td>
				<td>http://www.aragonés.com/</td>
				<td>3096568476741736-20/06</td>
				<td>8ea8e0b41e5e08398c465afce4ce4ae475668102</td>
				<td>Alfredo</td>
				<td>Tapia</td>
				<td>Irlanda-09209-Pasaje Julian Márquez-3</td>
				<td>football
movies
animals
comics
</td>
				<td>1997-07-12</td>
			</tr>

			<tr>
				<td>adrianagibert</td>
				<td>dolores29@yahoo.com</td>
				<td>http://noriega.info/</td>
				<td>869905548927649-24/01</td>
				<td>c2cc351923fa16d5619b62e0481a2d437c3a26c2</td>
				<td>Juan José</td>
				<td>Ropero</td>
				<td>Irlanda-48748-Via de Ángel Corominas-610</td>
				<td>movies
animals
books
comics
</td>
				<td>1997-10-31</td>
			</tr>
		</table>
		<h2><a href= "http://localhost:8080/"> Volver a la pagina inicial</a></h2>
	</body>
</html>