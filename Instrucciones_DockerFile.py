print("INSTRUCCIONES BÁSICAS DE DOCKERFILE")
# FROM [imagen_base]: Especifica la imagen base desde la cual se construirá la nueva imagen.
# RUN [comando]: Ejecuta un comando dentro de la imagen durante el proceso de construcción.
# COPY [origen] [destino]: Copia archivos o directorios desde el sistema
# WORKDIR [ruta]: Establece el directorio de trabajo para las instrucciones siguientes.
# CMD [comando]: Especifica el comando que se ejecutará cuando se inicie un contenedor a partir de la imagen.
# ENTRYPOINT [comando]: Define el comando principal que se ejecutará cuando se inicie un contenedor.
# ENV [variable] [valor]: Establece una variable de entorno dentro de la imagen
# docker build -t [nombre_imagen] . : Construye una imagen de Docker a partir del Dockerfile en el directorio actual y le asigna un nombre.

#------------------------------------------------------------------------------------------
# vim: Especifica el editor de texto Vim para ser instalado en la imagen. --> vim dockerfile or vim index.html
# :wq: Comando de Vim para guardar y salir del editor.