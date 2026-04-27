print("DOCKER SWARM")
# Docker Swarm es una herramienta de orquestación de contenedores que permite gestionar un clúster de Docker. 
# Con Docker Swarm, puedes desplegar y administrar aplicaciones distribuidas en múltiples hosts Docker, 
# lo que facilita la escalabilidad y la alta disponibilidad.

# En docker hay managers y workers, los managers son los nodos que controlan el clúster y toman decisiones sobre 
# la distribución de tareas, mientras que los workers son los nodos que ejecutan las tareas asignadas por los managers.

#Docker Swarm utiliza servicios para definir las aplicaciones que se ejecutarán en el clúster. Un servicio es 
# una definición de cómo se debe ejecutar un contenedor, incluyendo la imagen, las variables de entorno, 
# los puertos expuestos, entre otros parámetros.

#Tipos de servicios en Docker Swarm:
# 1. Replicated: Este tipo de servicio crea múltiples réplicas de un contenedor para garantizar la alta disponibilidad y la escalabilidad.
# 2. Global: Este tipo de servicio asegura que haya una instancia del contenedor en cada nodo del clúster, lo que es útil para servicios que necesitan estar presentes en todos los nodos, como agentes de monitoreo o servicios de registro.
# 3. Docker Stacks: Permite desplegar aplicaciones completas utilizando archivos de configuración YAML, lo que facilita la gestión de aplicaciones complejas con múltiples servicios.

# para inicializar un clúster de Docker Swarm se puede usar el comando:docker swarm init
# para unir un nodo al clúster se puede usar el comando:docker swarm join --token [token] [ip_nodo_manager]:2377
# para crear un servicio en Docker Swarm se puede usar el comando:docker service create --name [nombre_servicio] [imagen]
# para listar los servicios en Docker Swarm se puede usar el comando:docker service ls
# para escalar un servicio en Docker Swarm se puede usar el comando:docker service scale [nombre_servicio]=[número_replicas]
# para eliminar un servicio en Docker Swarm se puede usar el comando:docker service rm [nombre_servicio]
# para inspeccionar un servicio en Docker Swarm se puede usar el comando:docker service inspect [nombre_servicio]
# para listar las tareas de un servicio en Docker Swarm se puede usar el comando:docker service ps [nombre_servicio]
# para actualizar un servicio en Docker Swarm se puede usar el comando:docker service update [nombre_servicio] [opciones_actualización]
# para listar los nodos en el clúster de Docker Swarm se puede usar el comando:docker node ls
# para eliminar un nodo del clúster de Docker Swarm se puede usar el comando:docker node rm [nombre_nodo]
# para salir del clúster de Docker Swarm se puede usar el comando:docker swarm leave
# para forzar a un nodo a salir del clúster de Docker Swarm se puede usar el comando:docker swarm leave --force
# logs de un servicio en Docker Swarm se puede usar el comando:docker service logs [nombre_servicio]
# Para listar los contenedores en ejecución en Docker Swarm se puede usar el comando:docker ps
# para volver a la version anterior de un servicio en Docker Swarm se puede usar el comando:docker service rollback [nombre_servicio]
# para parar un servicio en Docker Swarm se puede usar el comando:docker service scale [nombre_servicio]=0

print("DCOKER STACKS")
# Docker Stacks es una característica de Docker Swarm que permite desplegar aplicaciones completas utilizando archivos de configuración YAML.
# Con Docker Stacks, puedes definir múltiples servicios, redes y volúmenes en un solo archivo YAML, lo que facilita la gestión de aplicaciones complejas con múltiples componentes.
# Para desplegar una aplicación utilizando Docker Stacks, puedes usar el comando:docker stack deploy -c [archivo_compose.yml] [nombre_stack]
# Para listar los stacks desplegados en Docker Swarm, puedes usar el comando:docker stack ls
# Para listar los servicios de un stack en Docker Swarm, puedes usar el comando:docker stack services [nombre_stack]
# Para eliminar un stack en Docker Swarm, puedes usar el comando:docker stack rm [nombre_stack]
# Para inspeccionar un stack en Docker Swarm, puedes usar el comando:docker stack ps [nombre_stack]
# Para actualizar un stack en Docker Swarm, puedes usar el comando:docker stack deploy -c [archivo_compose.yml] [nombre_stack] (con el mismo nombre de stack para actualizarlo)