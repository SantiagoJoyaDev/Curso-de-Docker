print("COMANDOS DOCKER")
# docker --version: Muestra la versión instalada de Docker en el sistema.
# docker pull [nombre_imagen]: Descarga una imagen de Docker desde Docker Hub.
# docker images: Lista todas las imágenes de Docker disponibles localmente en el sistema.
# docer run [nombre_imagen]: Crea y ejecuta un contenedor a partir de una imagen de Docker.
# docker ps: Muestra los contenedores en ejecución.
# cntrl + C: Detiene la ejecución de un contenedor en primer plano.
# docker ps -a: Muestra todos los contenedores, incluidos los detenidos.
# docker logs [nombre_contenedor]: Muestra los registros (logs) de un contenedor específico.
# docker stop [nombre_contenedor]: Detiene un contenedor en ejecución.
# docker start [nombre_contenedor]: Inicia un contenedor detenido.
# docker rm [nombre_contenedor]: Elimina un contenedor detenido.
# docker rm -f [nombre_contenedor]: Fuerza la eliminación de un contenedor en ejecución.
# docker rmi [nombre_imagen]: Elimina una imagen de Docker del sistema.
# docker rmi -f [nombre_imagen]: Fuerza la eliminación de una imagen, incluso si hay contenedores asociados.
# docker ps -s: Muestra el tamaño de los contenedores en ejecución.
#------------------------------------------------------------------------------------------
# docker run -d nombre_contenedor: Ejecuta el contenedor en segundo plano (detached mode).
# docker run -p [puerto_host]:[puerto_contenedor]: Mapea un puerto del host al puerto del contenedor.
# docker run -v [ruta_host]:[ruta_contenedor]: Monta un volumen del host en el contenedor.
# docker run --name [nombre_contenedor]: Asigna un nombre personalizado al contenedor.
# docker run --rm: Elimina automáticamente el contenedor cuando se detiene.
# docker run -e [variable_entorno]=[valor]: Establece una variable de entorno en el contenedor.
# docker run --env-file [ruta_archivo]: Carga variables de entorno desde un archivo.
#-------------------------------------------------------------------------------------------
# docker run --restart=always nombre_contenedor: Configura el contenedor para que se reinicie automáticamente si se detiene.
# docler run --restart=no nombre_contenedor: Desactiva el reinicio automático del contenedor.
# docker run --restart=unless-stopped nombre_contenedor: Reinicia el contenedor a menos que se detenga manualmente.
# docker run --restart=on-failure[:max-retries] nombre_contenedor: Reinicia el contenedor solo si termina con un error, con un número opcional de reintentos.
# docker run --restart=on-failure:<n> nombre_contenedor: Reinicia el contenedor solo si termina con un error, con un número específico de reintentos.
# docker exec -it nombre_contenedor /bin/bash: Abre una terminal interactiva dentro de un contenedor en ejecución.
# docker exec nombre_contenedor ls: Ejecuta un comando (en este caso, 'ls') dentro de un contenedor en ejecución.
# docker container prune: Elimina todos los contenedores detenidos para liberar espacio.
# docker image prune -a: Elimina todas las imágenes no utilizadas para liberar espacio.
# docker search [término_búsqueda]: Busca imágenes en Docker Hub que coincidan con el término de búsqueda proporcionado.
# docker commit [nombre_contenedor] [nombre_imagen]: Crea una nueva imagen a partir de los cambios realizados en un contenedor específico.
# docker save -o [archivo.tar] [nombre_imagen]: Guarda una imagen de Docker en un archivo tar para su distribución o respaldo.(exportar una imagen )
# docker load -i [archivo.tar]: Carga una imagen de Docker desde un archivo tar previamente guardado.(importar una imagen)
# docker tag [nombre_imagen] [nuevo_nombre]: Asigna un nuevo nombre o etiqueta a una imagen de Docker existente.
# docker volume create [nombre_volumen]: Crea un nuevo volumen de Docker para almacenar datos persistentes. 
# docker push [nombre_imagen]: Sube una imagen de Docker a un registro (como Docker Hub) para compartirla con otros usuarios.
# docker create volume [nombre_volumen]: Crea un nuevo volumen de Docker para almacenar datos persistentes.
# docker volume ls: Lista todos los volúmenes de Docker disponibles en el sistema.
# docker volume rm [nombre_volumen]: Elimina un volumen de Docker específico.
# docker volume prune: Elimina todos los volúmenes no utilizados para liberar espacio.
# docker volume -f [nombre_volumen]: Forza la eliminación de un volumen, incluso si está en uso por un contenedor.
#-------------------------------------------------------------------------------------------
print("COMANDOS DOCKER COMPOSE")
# docker compose up: Inicia los servicios definidos en un archivo docker-compose.yml.
# docker compose down: Detiene y elimina los contenedores, redes y volúmenes creados por docker compose up.
# docker compose build: Construye o reconstruye los servicios definidos en el archivo docker-compose.yml.
# docker compose logs: Muestra los registros (logs) de los servicios en ejecución.
# docker compose ps: Muestra el estado de los servicios definidos en el archivo docker-compose.yml.
# docker compose exec [nombre_servicio] [comando]: Ejecuta un comando dentro de un contenedor de un servicio específico.
# docker compose scale [nombre_servicio]=[número_replicas]: Escala un servicio a un número específico de réplicas.
# docker compose restart: Reinicia los servicios definidos en el archivo docker-compose.yml.
# docker compose stop: Detiene los servicios definidos en el archivo docker-compose.yml sin eliminar los contenedores.
# docker compose rm: Elimina los contenedores de los servicios definidos en el archivo docker-compose.yml sin detenerlos primero.
# docker compose config: Valida y muestra la configuración del archivo docker-compose.yml.
# docker compose pull: Descarga las imágenes necesarias para los servicios definidos en el archivo docker-compose.yml.
# docker compose push: Sube las imágenes de los servicios definidos en el archivo docker-compose.yml a un registro (como Docker Hub).
# docker compose version: Muestra la versión instalada de Docker Compose en el sistema.
# docker compose run [nombre_servicio] [comando]: Ejecuta un comando en un nuevo contenedor de un servicio específico, sin afectar a los contenedores en ejecución.
# docker compose up -d: Inicia los servicios en segundo plano (detached mode) definidos en el archivo docker-compose.yml.
# docker compose down --volumes: Detiene y elimina los contenedores, redes y volúmenes creados por docker compose up, incluyendo los volúmenes asociados.
# docker compose down --rmi all: Detiene y elimina los contenedores, redes y volúmenes creados por docker compose up, incluyendo todas las imágenes asociadas.
# docker compose -f [archivo_compose.yml] up: Inicia los servicios definidos en un archivo docker-compose.yml específico, lo que permite la creación de redes personalizadas para esos servicios.
# docker buildx build --platform [plataforma] -t [nombre_imagen] .: Construye una imagen de Docker para una plataforma específica utilizando Buildx, lo que permite la creación de imágenes multiplataforma.
# docker buildx create [nombre_builder]: Crea un nuevo builder de Buildx, lo que permite la construcción de imágenes para múltiples plataformas y arquitecturas.
# docker compose up --build: Inicia los servicios definidos en el archivo docker-compose.yml y reconstruye las imágenes si es necesario, lo que garantiza que se utilicen las versiones más recientes de las imágenes.
# docker compose up --force-recreate: Inicia los servicios definidos en el archivo docker-compose.yml y fuerza la recreación de los contenedores, incluso si no ha habido cambios en la configuración o las imágenes, lo que garantiza un entorno limpio y actualizado.
# docker compose up --no-deps: Inicia un servicio específico sin iniciar sus dependencias, lo que permite ejecutar solo el servicio deseado sin afectar a los servicios relacionados.
# quickly: docker compose up --scale [nombre_servicio]=[número_replicas]: Escala un servicio a un número específico de réplicas, lo que permite aumentar o disminuir la cantidad de contenedores en ejecución para ese servicio según las necesidades de carga o rendimiento.