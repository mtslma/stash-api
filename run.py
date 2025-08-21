import uvicorn
import os # Importamos o 'os'
from app.utils.network import get_local_ip

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    local_ip = get_local_ip()

    print("\n" + "="*50)
    print("🚀 INICIANDO SERVIDOR DA API 🚀")
    if os.environ.get("RENDER"):
        print("\n✅ Ambiente de Produção (Render) detetado.")
        print(f"   Servidor a escutar na porta: {port}")
    else:
        print(f"\n✅ API acessível em: http://{local_ip}:{port}")
        print(f"\n➡️  Copie este endereço: http://{local_ip}:{port}/api/extract")
    print("\n" + "="*50 + "\n")
    
    # Diz ao uvicorn para rodar na porta definida (10000 na Render, 8000 localmente)
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False) # 'reload=False' para produção