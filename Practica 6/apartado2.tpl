<!DOCTYPE html>
<html lang="es">
	<head>
		<title>Ruta optima</title>
		<meta charset="utf-8" />
	</head>
	<body>
	
		<h1>Introduzca el origen y el destino de la ruta:</h1>
	
		<form action="/apartado2" method="post">
            <h2>Calle origen: <input name="o_street" type="text" />
		    Numero origen: <input name="o_number" type="text" /></h2>
			<h2>Calle destino: <input name="d_street" type="text" />
		    Numero destino: <input name="d_number" type="text" /></h2>
		    <h2><input value="Enviar" type="submit" /></h2>
		</form>
		<h2><a href= "http://localhost:8080/"> Volver a la pagina inicial</a></h2>
	</body>
</html>