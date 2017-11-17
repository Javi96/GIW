<!DOCTYPE html>
<html lang="es">
	<head>
		<title>Practica 6</title>
		<meta charset="utf-8" />
	</head>
	<body>
		<ul>
		% for linea in texto:
			<li> {{linea}} </li>
		% end
		</ul>   
		<h2><a href= "http://localhost:8080/"> Volver a la pagina inicial</a></h2>
	</body>
</html>