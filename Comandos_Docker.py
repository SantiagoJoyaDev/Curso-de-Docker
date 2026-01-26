print("COMANDOS BÁSICOS DE DOCKER")
# docker --version: Muestra la versión instalada de Docker en el sistema.
# docker pull [nombre_imagen]: Descarga una imagen de Docker desde Docker Hub.
# docker images: Lista todas las imágenes de Docker disponibles localmente en el sistema.
# docer run [nombre_imagen]: Crea y ejecuta un contenedor a partir de una imagen de Docker.
# docker ps: Muestra los contenedores en ejecución.
# cntrl + C: Detiene la ejecución de un contenedor en primer plano.
# docker ps -a: Muestra todos los contenedores, incluidos los detenidos.
#docker logs [nombre_contenedor]: Muestra los registros (logs) de un contenedor específico.
# docker stop [nombre_contenedor]: Detiene un contenedor en ejecución.
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