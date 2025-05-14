import urllib.request
import zipfile
import os
from os import remove

# Caminho absoluto para a raiz do repositório
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Caminho para a pasta 'dados' dentro da raiz do repositório
dados_path = os.path.join(REPO_ROOT, "dados")
os.makedirs(dados_path, exist_ok=True)
print(f"Pasta 'dados' criada (ou já existia): {dados_path}")

# Caminho completo do arquivo zip
zip_path = os.path.join(dados_path, "telecom.zip")

# URL de download
url = 'https://www.kaggle.com/api/v1/datasets/download/oluwademiladeadeniyi/mtn-nigeria-customer-churn'
print("Baixando dataset...")
urllib.request.urlretrieve(url, zip_path)
print(f"Arquivo baixado em: {zip_path}")

# Extração dos arquivos
print("Extraindo conteúdo...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(dados_path)

# Lista de arquivos extraídos
print("Arquivos extraídos:")
for arquivo in os.listdir(dados_path):
    print("-", arquivo)

# Remoção do ZIP
remove(zip_path)
print("Arquivo ZIP removido.")
