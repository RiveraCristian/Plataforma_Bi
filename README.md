# Plataforma BI

Arquitectura base para una plataforma de análisis de datos al estilo Power BI/Looker. Incluye backend FastAPI modular, frontend React con TypeScript y despliegue mediante Docker Compose.

## Estructura

- `backend/`: Servicios FastAPI organizados por dominio (auth, catalog, connectors, semantic, query, scheduler, exporter) con SQLAlchemy y Pydantic.
- `frontend/`: Aplicación React + Vite con componentes para dashboards, editor drag-and-drop, filtros y métricas.
- `docker-compose.yml`: Orquesta Postgres, Redis, MinIO, backend y frontend.

## Puesta en marcha

### Script de desarrollo

Para ejecutar backend y frontend en modo desarrollo con un solo comando:

```bash
./scripts/start-dev.sh
```

El script valida que `poetry` y `yarn` estén disponibles, instala dependencias
si es necesario y levanta los servidores en `http://localhost:8000` (backend) y
`http://localhost:5173` (frontend). Usa `Ctrl+C` para detener ambos servicios.

### Ejecutar servicios manualment
```bash
# Backend
cd backend
poetry install
poetry run uvicorn app.main:app --reload

# Frontend
yarn install
yarn dev

# Docker Compose (servicios completos)
docker-compose up --build
```
