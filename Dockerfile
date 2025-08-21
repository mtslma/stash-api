# Imagem base
FROM python:3.11-slim

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do código
COPY . .

# Expõe a porta que a API vai usar
EXPOSE 10000

# Comando para iniciar a API quando o contêiner arrancar
CMD ["python", "run.py"]