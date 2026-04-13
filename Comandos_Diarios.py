print("COMANDOS DIARIOS DOCKER -- FLUJODE TRBAJO PROFESIONAL")

# =========================
# 🔍 1. INSPECCIÓN (SIEMPRE PRIMERO)
# =========================

# docker ps
# docker ps -a
# docker images

# =========================
# 🚀 2. PRIMERA VEZ (CREAR Y EJECUTAR)
# =========================

# mkdir -->Nombre de la carpeta la cual sera el app o proyecto
# cd ~/app-nginx
# docker run -d --name web_sepsi(nombre del proyecto) -p 8080:80 nginx(imagen a usar)

# =========================
# 🔁 3. USO DIARIO (SIN RECREAR)
# =========================

# docker stop web_sepsi
# docker start web_sepsi

# =========================
# 🧱 4. VERSIONADO PROFESIONAL
# =========================

# docker build -t web_sepsi .
# docker run -d --name web_v1 -p 8080:80 web_sepsi

# nueva versión

# docker build -t web_sepsi .
# docker run -d --name web_v2 -p 8081:80 web_sepsi

# =========================
# 🔁 5. ROLLBACK (VOLVER ATRÁS)
# =========================

# docker stop web_v2
# docker start web_v1

# =========================
# 🧪 6. DEBUG / VERIFICACIÓN
# =========================

# docker logs web_sepsi
# docker exec -it web_sepsi bash
# docker exec -it web_sepsi cat /usr/share/nginx/html/index.html

# =========================
# 🧹 7. LIMPIEZA NORMAL
# =========================

# docker rm web_sepsi
# docker rmi web_sepsi

# =========================
# 🔥 8. LIMPIEZA CUANDO HAY CAOS (RESET)
# =========================

# docker stop $(docker ps -q)
# docker rm -f $(docker ps -aq)
# docker image prune -a

# =========================
# 🚀 9. REINICIO LIMPIO
# =========================

# cd ~/app-nginx
# docker run -d --name web_sepsi -p 8080:80 -v $(pwd):/usr/share/nginx/html nginx