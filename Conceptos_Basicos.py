print("CONCEPTOS BÁSICOS DE DOCKER")

# Docker es una plataforma que permite crear, desplegar y ejecutar aplicaciones en contenedores.
# Un contenedor es una unidad estandarizada de software que empaqueta el código y todas sus dependencias para que la aplicación se ejecute de manera rápida y confiable en cualquier entorno.
# Docker file: es un archivo de texto que contiene una serie de instrucciones para construir una imagen de Docker.
# imagen: Es un archivo o una plantilla que contiene todo lo necesario para ejecutar una aplicación, incluyendo el código, las bibliotecas, las dependencias y el sistema operativo.
# Docker Hub: es un servicio de registro de imágenes de Docker en la nube que permite a los usuarios almacenar, compartir y distribuir imágenes de Docker.

#------------------------------------------------------------------------------------------
# Inmutabilidad en la imagenes de Docker: Las imágenes de Docker son inmutables, lo que significa que una vez que se crea una imagen, no se puede modificar. 
# Si se necesitan cambios, se debe crear una nueva imagen basada en la anterior.

# Capas de imagen: Las imágenes de Docker están compuestas por capas. Cada instrucción en un Dockerfile crea una nueva capa en la imagen.
# Esto permite la reutilización de capas comunes entre diferentes imágenes, lo que ahorra espacio y mejora la eficiencia.