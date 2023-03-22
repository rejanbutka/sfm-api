from fastapi import FastAPI
from app.routers.companies import router as company_router
from app.routers.employees import router as employee_router
from app.routers.farms import router as farm_router

def create_app() -> FastAPI:
    """
    Returns FastAPI instance
    """
    app = FastAPI()
    app.include_router(router=company_router)
    app.include_router(router=employee_router)
    app.include_router(router=farm_router)
    return app

app = create_app()