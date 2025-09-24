from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth, catalog, connectors, exporter, query, scheduler, semantic
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(title=settings.project_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=settings.api_v1_prefix)
app.include_router(catalog.router, prefix=settings.api_v1_prefix)
app.include_router(connectors.router, prefix=settings.api_v1_prefix)
app.include_router(semantic.router, prefix=settings.api_v1_prefix)
app.include_router(query.router, prefix=settings.api_v1_prefix)
app.include_router(scheduler.router, prefix=settings.api_v1_prefix)
app.include_router(exporter.router, prefix=settings.api_v1_prefix)


@app.get("/")
def healthcheck():
    return {"status": "ok"}
