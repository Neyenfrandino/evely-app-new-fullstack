# Aqui estamos creando una ruta para todas las rutas que se necesiten para el api
from fastapi import APIRouter
from typing import List, Optional

def api_router(prefix: str = "", tags: Optional[List[str]] = None):
    router = APIRouter(prefix=f"/{prefix}", tags=tags or [])
    return router
