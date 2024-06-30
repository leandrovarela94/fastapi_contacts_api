from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from routes import router 

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    yield
    # Lógica de limpeza após o yield


app = FastAPI(lifespan=lifespan)


app.include_router(router=router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8082, reload=True, workers=5)