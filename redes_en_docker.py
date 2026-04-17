print("Redes en Docker")
# Las redes en Docker permiten la comunicación entre contenedores y con el mundo exterior. Docker crea automáticamente una red bridge para cada contenedor, 
# pero también se pueden crear redes personalizadas para una mejor organización y seguridad.

# Tipos de redes en Docker:
# 1. Bridge: Es la red predeterminada para contenedores que no especifican una red. Permite la comunicación entre contenedores en la misma red y con el host.
# 2. Host: El contenedor comparte la red del host, lo que significa que el contenedor puede acceder a los servicios del host y viceversa. No hay aislamiento de red entre el contenedor y el host.
# 3. Overlay: Permite la comunicación entre contenedores en diferentes hosts Docker, lo que es útil para aplicaciones distribuidas y clústeres de Docker Swarm.
# 4. Macvlan: Permite asignar una dirección MAC a un contenedor, lo que le permite aparecer como un dispositivo físico en la red. Esto es útil para aplicaciones que requieren una dirección IP dedicada.
# 5. None: El contenedor no tiene acceso a la red, lo que significa que no puede comunicarse con otros contenedores ni con el host.

# para crear una red personalizada se puede usar el comando:docker network create [nombre_red]
# para conectar un contenedor a una red se puede usar el comando:docker network connect [nombre_red] [nombre_contenedor]
# para inspeccionar una red se puede usar el comando:docker network inspect [nombre_red]
# para eliminar una red se puede usar el comando:docker network rm [nombre_red]
# para conectar un contenedor a una red al momento de crear el contenedor se puede usar el comando:docker run --network [nombre_red] [imagen]
# para que un contenedor tenga doble conexión a redes se puede usar el comando:docker network connect [nombre_red] [nombre_contenedor]
# para desconectar un contenedor de una red se puede usar el comando:docker network disconnect [nombre_red] [nombre_contenedor]
# para eliminar todas las redes no utilizadas se puede usar el comando:docker network prune
# para listar todas las redes se puede usar el comando:docker network ls
# para listar los contenedores conectados a una red se puede usar el comando:docker network inspect [nombre_red] --format '{{range .Containers}}{{.Name}} {{end}}'
