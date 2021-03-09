
build:
	docker image build -t alvaroms/template-microservice:v1.0 .

run:
	docker container run -d --name template-microservice -p 6060:80 alvaroms/template-microservice:v1.0

exec:
	docker container exec -it template-microservice /bin/sh

logs:
	docker container logs template-microservice

test:
	pytest --setup-show

all: test build run