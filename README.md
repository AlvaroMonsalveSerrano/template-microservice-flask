# Template-microservices

## Introducción

Ejemplo de creación de una plantilla para un microservicio.

Todo el código definido en el proyecto tiene como objetivo describir elementos básicos necesarios
con una finalidad didáctica.

## Creación

    1.- Creación de la carpeta del proyecto.
    2.- Creación del fichero README.md
    3.- Creación del fichero requirements.txt
    4.- Creación del entorno virtual.
      4.1.- Creación del entorno: $>virtualenv -p python3.6 .venv
      4.2.- Activar el entorno: $>source .venv/bin/activate
      4.3.- Para desactivar el entorno: $>desactivate
    
      El entorno virtual se instala en la carpeta .venv del proyecto.
    
    4.- Definición del fichero de requerimientos
    
    El fichero requirements.txt localizado en la raíz del proyecto, define todas aquellas dependencias de librerías
    necesarias para realizar la funcionalidad del proyecto    
    
    5.- Instalación d elas dependencias: $>pip install -r requirements.txt  

## Test

```
pytest --setup-show
```


## Run

Hay dos formas de arrancar la aplicación, en las dos formas, hay que ubicarse en la carpeta del proyecto:

1.- Definiendo una variable de entorno de forma explicita:
```
cd entrypoints/
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

2.- Definiendo la variable de entorno de forma implícita.
```
cd entrypoints/
FLASK_ENV=development FLASK_DEBUG=0 FLASK_APP=app.py flask run
```

Para probar los endpoint:

```
curl http://localhost:5000/
curl http://localhost:5000/readiness
curl http://localhost:5000/liveness
curl --header "Content-Type: application/json" --request POST \
     --data '{"name":"xyz1", "operation":"+", "operator":"20"}' \
     http://localhost:5000/use_case_example
```

## Docker 

1.- Creación de la imagen.
``` 
docker image build -t alvaroms/template-microservice:v1.0 .
```

2.- Arrancar el contenedor.
``` 
docker container run -d --name template-microservice -p 6060:80 alvaroms/template-microservice:v1.0
```

3.- Entrar en la consola del contenedor.
``` 
docker container exec -it template-microservice /bin/sh
```

4.- Visualizar los logs del contenedor.
``` 
docker container logs template-microservice
```

Para probar los endpoints de la aplicación arrancada en el contenedor, se pueden utilizar los siguientes comandos curl:

```
curl http://localhost:6060/
curl http://localhost:6060/liveness
curl http://localhost:6060/rediness
curl --header "Content-Type: application/json" --request POST \
     --data '{"name":"xyz1", "operation":"+", "operator":"20"}' \
     http://localhost:6060/use_case_example
```

