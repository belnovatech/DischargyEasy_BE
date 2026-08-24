from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import advisor
from app.routers import contact
from app.routers import reimbursement



Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="DischargeEasy API"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "https://discharge-easy.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(advisor.router)
app.include_router(contact.router)
app.include_router(reimbursement.router)


@app.get("/")
def root():
    return {
        "message": "DischargeEasy API is running"
    }