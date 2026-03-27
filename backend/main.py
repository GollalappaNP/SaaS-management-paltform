from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.db.database import engine, Base
from backend.api import subscriptions, wallet, employees, agents

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SaaS Management Platform",
    description="Intelligent SaaS Management with Finance Wallet and AI Agents",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(subscriptions.router)
app.include_router(wallet.router)
app.include_router(employees.router)
app.include_router(agents.router)

@app.get("/")
def root():
    return {"message": "SaaS Management Platform is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}