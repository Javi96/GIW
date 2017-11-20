<!DOCTYPE html>
<html lang="es">
	<head>
		<title>Paradas de bus</title>
		<meta charset="utf-8" />
	</head>
	<body>
	
		<h1>Introduzca el origen y el destino de la ruta:</h1>
		<form action="/service3" method="post">
            <h2>Calle : <input name="street" type="text" />
		    Numero : <input name="number" type="text" /></h2>
		    <h2><input value="Enviar" type="submit" /></h2>
		</form>
		<h2><a href= "http://localhost:8080/"> Volver a la pagina inicial</a></h2>
	</body>
</html>