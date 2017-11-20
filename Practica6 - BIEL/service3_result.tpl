<!DOCTYPE html>
<html lang="es">
	<head>
		<title>Paradas de bus</title>
		<meta charset="utf-8" />
	</head>
	<body>
		<h1>Paradas de bus cercanas: </h1>
		<ul>
		% for linea in texto:
			<h2> {{linea}} </h2>
		% end
		</ul>   
		<h2><a href= "http://localhost:8080/"> Volver a la pagina inicial</a></h2>
	</body>
</html>