print("INSTRUCCIONES BÁSICAS DE DOCKERFILE")
# FROM [imagen_base]: Especifica la imagen base desde la cual se construirá la nueva imagen.
# RUN [comando]: Ejecuta un comando dentro de la imagen durante el proceso de construcción.
# COPY [origen] [destino]: Copia archivos o directorios desde el sistema
# WORKDIR [ruta]: Establece el directorio de trabajo para las instrucciones siguientes.
# CMD [comando]: Especifica el comando que se ejecutará cuando se inicie un contenedor a partir de la imagen.
# ENTRYPOINT [comando]: Define el comando principal que se ejecutará cuando se inicie un contenedor.
# ENV [variable] [valor]: Establece una variable de entorno dentro de la imagen
# docker build -t [nombre_imagen] . : Construye una imagen de Docker a partir del Dockerfile en el directorio actual y le asigna un nombre el punto es necesario.
# ARG [nombre_argumento]: Define un argumento que se puede pasar durante la construcción de la imagen.

#------------------------------------------------------------------------------------------
# vim: Especifica el editor de texto Vim para ser instalado en la imagen. --> vim dockerfile or vim index.html
# :wq: Comando de Vim para guardar y salir del editor.
#------------------------------------------------------------------------------------------
# hacer un enttypoint con un script bash:
# 1. crear la imagen con docker build -t [nombre_imagen] .
# 2. crear el contenedor con docker run --name [nombre_contenedor] -d [nombre_imagen]
# 3. verificar que el contenedor este corriendo con docker ps
# 4. acceder al contenedor con docker exec -it [nombre_contenedor] /bin/bash
# 5. dentro del contenedor, crear un script bash, por ejemplo: 
# FROM ALPINE
# ENTRYPOINT ["echo","Hola"]
# CMD ["Mundo"]
# 6. guardar el archivo y salir de vim con :wq

#------------------------------------------------------------------------------------------
# esto es para probar ARG y ENTRYPOINT lo que hace es crear un archivo message con un mensaje personalizado y luego mostrarlo al ejecutar el contenedor.
#FROM alpine

#ARG NOMBRE=SantiagoJoya

#run echo "hola $NOMBRE" > message

#ENTRYPOINT ["cat","message"]
# lo importante del ARG aqui es que se puede pasar un valor diferente al construir la imagen con --build-arg NOMBRE=OtroNombre esto permite personalizar el mensaje sin modificar 
# el Dockerfile.