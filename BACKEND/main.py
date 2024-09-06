from fastapi import FastAPI
import uvicorn
from app.routers.user import user
from app.db.database import Base, engine 

app = FastAPI()

def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()

app.include_router(user.router)

#if __name__ == "__main__":
#    uvicorn.run('main:app', port=8000, reload=True)
