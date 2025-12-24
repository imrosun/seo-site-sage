from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.routes import router
from app.db.session import engine
from app.db.base import Base
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("site-sage")

app = FastAPI(
    title="Site Sage API",
    description="SEO and performance analyzer",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        logger.exception("Database startup failed")
        raise

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception")
    return JSONResponse(
        status_code=500,
        content={
            "error": "INTERNAL_SERVER_ERROR",
            "message": str(exc),
            "path": request.url.path,
        },
    )

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}

app = app  # required for Vercel
