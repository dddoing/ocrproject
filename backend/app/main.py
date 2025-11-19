"""
FastAPI main application entry point
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes
from app.core.config import settings

app = FastAPI(
    title="Universal Document Translator API",
    description="AI-powered document OCR, translation, and analysis",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routes.router, prefix="/api")


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Universal Document Translator API",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "database": "connected",  # TODO: Add actual DB check
        "redis": "connected",     # TODO: Add actual Redis check
    }
