from fastapi import FastAPI
from app.routers import videos

app = FastAPI(
    title="Stash Media Extractor API",
    description="API para extrair links de mídia de várias fontes.",
    version="1.0.0"
)

# Inclui o router de vídeos na aplicação principal
app.include_router(videos.router, prefix="/api", tags=["Videos"])   