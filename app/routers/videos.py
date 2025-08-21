from fastapi import APIRouter, HTTPException
from ..schemas.video import VideoRequest, VideoResponse
from ..services.extractor import extract_media_info

router = APIRouter()

@router.post(
    "/extract", 
    response_model=VideoResponse,
    summary="Extrai links de mídia de uma URL", # <-- Título curto
    description="Recebe uma URL de um site suportado (Instagram, Twitter, etc.) e retorna os links diretos para o vídeo e thumbnail."
)
def extract_video_endpoint(req: VideoRequest):
    """
    Este endpoint processa uma URL para extrair informações de mídia.
    - **url**: O link completo para o post, reel, ou vídeo.
    """
    try:
        return extract_media_info(req.url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao processar: {str(e)}")