print("COMANDOS DIARIOS DOCKER -- FLUJODE TRBAJO PROFESIONAL")
print("ORDEN PROFESIONAL CON VERSIONAMIENTO")

# 🧭 FLUJO ESTRUCTURADO PROFESIONAL (REORDENADO)

# =========================
# 📦 1. CREAR PROYECTO (BASE LOCAL)
# =========================

# mkdir app-python
# cd app-python


# =========================
# 📄 2. CREAR SCRIPT PYTHON
# =========================

# vim script.py


# =========================
# 📦 3. DEPENDENCIAS
# =========================

# vim requirements.txt


# =========================
# 🐳 4. DOCKERFILE
# =========================

# vim Dockerfile


# =========================
# 🐳 5. BUILD + VERSIONAMIENTO DE IMAGEN
# =========================

# docker build -t app-python:v1 .

# ✔️ Aquí creas la primera versión de la imagen


# =========================
# 🚀 6. CREAR Y EJECUTAR CONTENEDOR (v1)
# =========================

# docker run -d --name app-python-v1 -p 8080:80 test-python:v

# ✔️ Contenedor creado desde la imagen v1


# =========================
# 🔁 7. NUEVA VERSIÓN (v2) - MODIFICAR CÓDIGO
# =========================

# vim script.py


# =========================
# 🐳 8. RE-BUILD IMAGEN v2
# =========================

# docker build -t app-python:v2 .


# =========================
# 🚀 9. EJECUTAR CONTENEDOR v2
# =========================

# docker run --name app-python-v2 -d app-python:v2

# 🧹 🐳 DOCKER - COMANDOS DE BORRADO (RESUMEN DESDE 10)

# =========================
# 10. BORRAR UN CONTENEDOR ESPECÍFICO
# =========================

# docker rm -f nombre_contenedor


# =========================
# 11. BORRAR TODOS LOS CONTENEDORES
# =========================

# docker rm -f $(docker ps -aq)


# =========================
# 12. BORRAR UNA IMAGEN ESPECÍFICA
# =========================

# docker rmi -f nombre-imagen:tag


# =========================
# 13. BORRAR TODAS LAS IMÁGENES
# =========================

# docker rmi -f $(docker images -q)


# =========================
# 14. LIMPIEZA TOTAL (RECOMENDADO)
# =========================

# docker system prune -a --volumes -f


# =========================
# 15. BORRAR REDES NO USADAS
# =========================

# docker network prune -f


# =========================
# 16. BORRAR VOLUMENES
# =========================

# docker volume prune -f


# =========================
# 🧠 RESUMEN CLAVE
# =========================

# - rm -f → contenedores
# - rmi -f → imágenes
# - system prune → limpieza total del sistema Docker

# =========================
# 🧠 RESUMEN PROFESIONAL REAL
# =========================

# 1. Creas carpeta del proyecto
# 2. Escribes código
# 3. Construyes imagen (versionada)
# 4. Ejecutas contenedor desde imagen
# 5. Modificas código
# 6. Repetir build + run