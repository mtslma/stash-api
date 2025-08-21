from pydantic import BaseModel
from typing import Optional

class VideoRequest(BaseModel):
    url: str

class VideoResponse(BaseModel):
    status: str
    requested_url: str
    video_url: Optional[str] = None
    audio_url: Optional[str] = None
    thumbnail_url: Optional[str] = None