# Biblioteca demo

Web App de consulta de un libro ficticio. Docker Compose ejecuta dos servicios a partir de la misma imagen Python. **web** sirve HTML y obtiene el título de **catalog**. Solo web publica un puerto y lo liga al loopback del host. Ambos procesos usan un usuario sin privilegios.

## Ejecutar y demostrar

```sh
docker compose up -d --build
docker compose ps
curl -fsS http://localhost:8080/health
curl -fsS http://localhost:8080/
```

Abre `http://localhost:8080/`. En un entorno remoto, reenvía el puerto 8080 de forma privada. Para detener la demo, ejecuta `docker compose down`. `.env.example` documenta el puerto opcional `WEB_PORT`.

## Pipeline y registro

El [workflow](.github/workflows/devsecops.yml) se ejecuta al enviar cambios a `main` o manualmente.

1. **verify** valida Compose y prueba salud, consulta real al catálogo y respuesta 404.
2. **build** construye la imagen con la etiqueta del commit y la exporta como artefacto para el siguiente job.
3. **publish** recupera la misma imagen, se autentica con el token temporal del workflow y la publica en `ghcr.io/propietario/repositorio:<sha>`. El permiso de escritura en Packages se concede solo a este job.

La evidencia de ejecución está en la pestaña **Actions** del repositorio. Abre la corrida del commit entregado y el log de **publish** para ver el digest. En **Packages**, abre la versión etiquetada con ese SHA. Si el paquete es privado, concede al docente acceso de lectura o haz visible el paquete de la demo.

## Seguridad

Consulta el [DFD y la matriz STRIDE](docs/seguridad.md).
