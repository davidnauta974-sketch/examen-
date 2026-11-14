# Guion de grabación

Graba cinco clips cortos de pantalla, uno por bloque. Puedes narrar en directo o guardar el audio de cada bloque con el mismo número. Duración objetivo de 4 a 5 minutos.

## 01 · README y propósito · 35 s

**Muestra** el README renderizado en GitHub.

«Presento Biblioteca demo, una aplicación que consulta un catálogo y muestra un libro disponible. Separé la interfaz web del catálogo para demostrar cómo dos servicios se comunican dentro de Docker Compose. La imagen es la misma para ambos. La variable CATALOG_URL indica qué instancia actúa como web.»

## 02 · Docker Compose · 55 s

**Muestra** docker-compose.yml, Dockerfile, la salida real de docker compose ps y la página abierta.

«Compose configura web y catalog. Web publica el puerto 8080 en loopback y consulta catalog por su nombre dentro de la red backend. El catálogo no publica puertos al host. En el Dockerfile copio el código sobre una base Python y ejecuto el proceso como usuario sin privilegios. Aquí se ven ambos servicios activos y la página muestra el dato recibido del catálogo.»

## 03 · Código del pipeline · 65 s

**Muestra** .github/workflows/devsecops.yml y desplázate por los tres jobs.

«El pipeline arranca cuando se actualiza main. Verify valida Compose, inicia el entorno y comprueba el endpoint de salud, el título del libro y una ruta inexistente. Build se ejecuta después y guarda la imagen como artefacto etiquetado por commit. Publish descarga ese mismo artefacto, lo etiqueta para GHCR y lo sube usando el token temporal de GitHub. Únicamente publish tiene permisos de escritura en Packages.»

## 04 · Evidencia real · 45 s

**Muestra** la corrida verde en Actions, el log de publish y la versión del paquete en GHCR. Graba este bloque después de verificar que aparecen.

«Aquí están las etapas verify, build y publish de la corrida. En el log se observa el digest después de publicar. En Packages puedo consultar la imagen con la etiqueta del commit. Eso permite vincular lo que se publicó con el código de esta ejecución.»

## 05 · DFD, STRIDE y cierre · 75 s

**Muestra** docs/seguridad.md renderizado. Haz zoom si se necesita.

«El DFD muestra el navegador, web, catálogo, su dato ficticio y la cadena de publicación. Los límites separan el host Docker, la red interna, GitHub y el registro. Para suplantación, el catálogo queda en la red interna y se podría autenticar en producción. Para manipulación, la imagen se asocia al commit y propongo proteger main y verificar el digest. Para repudio, Actions registra el actor y la ejecución. Para divulgación, limito el acceso al puerto y uso datos ficticios. Para denegación de servicio, la consulta tiene un timeout. Para elevación de privilegios, los procesos corren sin root y el permiso de publicación se limita a un job.»

## Entrega

Sube el MP4 como video no listado, o a Drive con acceso de lectura por enlace. Comprueba en una ventana privada el video y el repositorio, o verifica el acceso concedido al docente. Entrega ambos enlaces. Comparte para edición los clips de pantalla y tu voz en archivos numerados 01 a 05.
