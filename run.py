# run.py
import uvicorn
from app.utils.network import get_local_ip

if __name__ == "__main__":
    local_ip = get_local_ip()
    port = 8000
    
    print("\n" + "="*50)
    print("🚀 INICIANDO SERVIDOR DA API 🚀")
    print(f"\n✅ API estará acessível em: http://{local_ip}:{port}")
    print("\n➡️  Endereço para requisições de download:")
    print(f"   http://{local_ip}:{port}/api/extract")
    print("\n" + "="*50 + "\n")
    
    # Diz ao uvicorn para rodar o objeto 'app' que está dentro do ficheiro 'main.py'
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)