# 📦 Stash API

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-green?style=for-the-badge&logo=fastapi&logoColor=white)
![yt-dlp](https://img.shields.io/badge/yt--dlp-LATEST-purple?style=for-the-badge)

API de extração de mídias para o aplicativo Stash. Este serviço backend é responsável por receber uma URL de uma rede social e retornar os links diretos para o conteúdo de vídeo, áudio e thumbnails.

---

### 🚀 Funcionalidades Principais

-   **Extração de URL**: A API aceita uma URL de vídeo e extrai o link direto para o arquivo de vídeo e áudio.
-   **Extração de Miniatura (Thumbnail)**: Retorna a URL da miniatura do vídeo, ideal para pré-visualização.
-   **Suporte a Múltiplas Plataformas**: Utiliza o poder do `yt-dlp`, o que significa que funciona com uma vasta gama de sites, incluindo YouTube, Twitter, Instagram e muitos outros.

---

### ⚙️ Setup e Execução

Para rodar a API localmente, siga os passos abaixo.

#### Pré-requisitos

Certifique-se de ter o Python 3.7+ instalado.

#### 1. Clonar o repositório

```bash
git clone https://github.com/mtslma/stash-api.git
cd stash-api
```

#### 2. Instalar as dependências

Crie um ambiente virtual (recomendado) e instale os pacotes necessários a partir do arquivo `requirements.txt`.

##### Linux

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

##### Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### 3. Executar o servidor

A API pode ser iniciada a partir do comando:

```bash
python run.py
```

Ao iniciar, o servidor exibirá o endereço de IP e a porta onde a API está acessível.

```
==================================================
🚀 INICIANDO SERVIDOR DA API 🚀

✅ API estará acessível em: http://<seu_ip>:8000

➡️ Endereço para requisições de download: http://<seu_ip>:8000/extract

==================================================
```

---

### 💡 Como usar a API

A API expõe um único endpoint `POST` para extração de vídeo.

#### Endpoint: `/extract`

-   **Método**: `POST`
-   **URL**: `http://<seu_ip>:8000/extract`
-   **Corpo da Requisição (JSON)**:
    ```json
    {
        "url": "https://www.youtube.com/watch?v=4Ukh9aQBzWc"
    }
    ```
-   **Resposta esperada**:
    ```json
    {
        "status": "sucesso",
        "requested_url": "https://www.youtube.com/watch?v=4Ukh9aQBzWc",
        "video_url": "https://rr16---sn-8p8v-bg0z.googlevideo.com/videoplayback?...",
        "audio_url": null,
        "thumbnail_url": "https://i.ytimg.com/vi_webp/4Ukh9aQBzWc/maxresdefault.webp"
    }
    ```
