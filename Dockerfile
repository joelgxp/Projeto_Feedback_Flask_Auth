# Use a imagem base do Python
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependêUNias do projeto
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# Copia o conteúdo do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Expõe a porta 5000 para acessar o aplicativo Flask
ENV PORT 5000

# Comando para executar o aplicativo Flask quando o contêiner for iniciado
CMD ["python", "main.py"]
