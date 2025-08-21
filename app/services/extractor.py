import yt_dlp
from ..schemas.video import VideoResponse

def extract_media_info(url: str) -> VideoResponse:
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        video_url = None
        audio_url = None

        if "formats" in info:
            # Pega melhor vídeo com áudio junto
            for f in reversed(info["formats"]):
                if f.get("acodec") != "none" and f.get("vcodec") != "none":
                    video_url = f["url"]
                    break
            
            # Pega melhor áudio isolado (se não encontrou vídeo com áudio)
            if not video_url:
                 for f in reversed(info["formats"]):
                    if f.get("acodec") != "none" and f.get("vcodec") == "none":
                        audio_url = f["url"]
                        break
        
        thumbnail_url = info.get("thumbnail")

        return VideoResponse(
            status="sucesso",
            requested_url=url,
            video_url=video_url,
            audio_url=audio_url,
            thumbnail_url=thumbnail_url
        )