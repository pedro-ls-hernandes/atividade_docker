FROM python:3.13 
#Define a imagem base para python

WORKDIR /app
#Define o diretório de trabalho dentro do container para /app

COPY requirements.txt .
#Copia o arquivo requirements.txt para o diretório de trabalho no container

RUN python -m pip install -r requirements.txt
#Executa o código que instala as dependências listadas no requirements.txt

COPY . .
#Copia os demais arquivos

EXPOSE 80
#Define a porta do container para 80

CMD ["python", "index.py"]
#Executa o código que inicia o arquivo dentro do container