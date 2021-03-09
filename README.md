# Template-microservices

## Introduction

Example of creating a template for a microservice developed in Python with the Flask library.

All the code defined in the project aims to describe necessary basic elements
with a didactic purpose.

## Creation

     1.- Creation of the virtual environment.
       1.1.- Creation of the environment: $> virtualenv -p python3.6 .venv
       1.2.- Activate the environment: $> source .venv / bin / activate
       1.3.- To deactivate the environment: $> deactivate
    
       The virtual environment is installed in the project's .venv folder.
    
     2.- Installing the dependencies: $> pip install -r requirements.txt


## Test

```
pytest --setup-show
```

## Run

There are two ways to start the application, in both ways, it must be located in the project folder:

1.- Defining an environment variable explicitly:
```
cd entrypoints /
export FLASK_APP = app.py
export FLASK_ENV = development
flask run
```

2.- Defining the environment variable implicitly.
```
cd entrypoints /
FLASK_ENV = development FLASK_DEBUG = 0 FLASK_APP = app.py flask run
```

To test the endpoints:

```
curl http: // localhost: 5000 /
curl http: // localhost: 5000 / readiness
curl http: // localhost: 5000 / liveness
curl --header "Content-Type: application / json" --request POST \
      --data '{"name": "xyz1", "operation": "+", "operator": "20"}' \
      http: // localhost: 5000 / use_case_example
```


## Docker

1.- Image creation. Operation ** build ** of the Makefile file.
```
docker image build -t alvaroms / template-microservice: v1.0.

> make build
```

2.- Start the container. Operation ** run ** of the Makefile file.
```
docker container run -d --name template-microservice -p 6060: 80 alvaroms / template-microservice: v1.0

> make run
```

3.- Enter the container console. Operation ** exec ** of the Makefile file.
```
docker container exec -it template-microservice / bin / sh

> make exec
```

4.- View the container logs. Operation ** logs ** of the Makefile file.
```
docker container logs template-microservice

> make logs
```

5.- For the joint execution of the basic operations: test, creation of the image and boot
the ** all ** command from the Makefile is used.

```
> make all
```

To test the endpoints of the application started in the container, the following curl commands can be used:

```
curl http: // localhost: 6060 /
curl http: // localhost: 6060 / liveness
curl http: // localhost: 6060 / rediness
curl --header "Content-Type: application / json" --request POST \
     --data '{"name": "xyz1", "operation": "+", "operator": "20"}' \
     http: // localhost: 6060 / use_case_example
```


---

# Template-microservices

## Introducción

Ejemplo de creación de una plantilla para un microservicio desarrollado en Python con la librería Flask.

Todo el código definido en el proyecto tiene como objetivo describir elementos básicos necesarios
con una finalidad didáctica.

## Creación

    1.- Creación del entorno virtual.
      1.1.- Creación del entorno: $>virtualenv -p python3.6 .venv
      1.2.- Activar el entorno: $>source .venv/bin/activate
      1.3.- Para desactivar el entorno: $>desactivate
    
      El entorno virtual se instala en la carpeta .venv del proyecto.
    
    2.- Instalación d elas dependencias: $>pip install -r requirements.txt  

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

1.- Creación de la imagen. Operación **build** del fichero Makefile.
``` 
docker image build -t alvaroms/template-microservice:v1.0 .

>make build
```

2.- Arrancar el contenedor. Operación **run** del fichero Makefile.
``` 
docker container run -d --name template-microservice -p 6060:80 alvaroms/template-microservice:v1.0

>make run
```

3.- Entrar en la consola del contenedor. Operación **exec** del fichero Makefile.
``` 
docker container exec -it template-microservice /bin/sh

>make exec
```

4.- Visualizar los logs del contenedor. Operación **logs** del fichero Makefile.
``` 
docker container logs template-microservice

> make logs
```

5.- Para la ejecución conjunto de las operaciones básicas: test, creación de la imagen y arranque
se emplea el comando **all** del fichero Makefile.

```
>make all
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

