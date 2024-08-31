from src.databases.database import db_engine, Base
from src.routers import routers
from fastapi import FastAPI
from src.graphql.schema import graphql_app

Base.metadata.create_all(bind=db_engine)

app = FastAPI(
    title="🪼 Vessel: Marine Product CRUD API",
    version="2.0"
)
app.include_router(graphql_app, prefix="/graphql")
app.include_router(routers.router)

@app.on_event("startup")
async def startup():
    # start the database
    Base.metadata.create_all(bind=db_engine)
    print("Database Marine Product Connected")

@app.on_event("shutdown")
async def shutdown():
    db_engine.dispose()
    print("Database Marine Product Disconnected")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)