**Análise de Dados com Spark**

Este projeto realiza uma análise exploratória de dados de uma empresa de telecomunicações que oferece serviços de internet fixa e móvel. A análise foi feita utilizando PySpark. 
O conjunto de dados pode ser encontado no Kaggle através do link: https://www.kaggle.com/datasets/oluwademiladeadeniyi/mtn-nigeria-customer-churn.

🗂️ Origem dos Dados

Os dados foram extraídos automaticamente do Kaggle utilizando a API oficial.
⚠️ Importante: Para utilizar a API do Kaggle, é necessário ter uma conta e configurar sua chave de autenticação:

Acesse: https://www.kaggle.com/account

Clique em "Create New API Token"

Salve o arquivo kaggle.json em ~/.kaggle/ (Linux/Mac) ou %USERPROFILE%\.kaggle\ (Windows)

O dataset utilizado contém as seguintes colunas: 

**Customer ID**: um identificador exclusivo atribuído a cada cliente. Pode aparecer mais de uma vez se o cliente possuir vários dispositivos.

**Full Name**: O nome completo do cliente. Os nomes refletem o equilíbrio entre etnias e regiões nigerianas.

**Date of Purchase**: mês e ano em que o dispositivo ou plano foi adquirido. Todos os dados são de 2025.

**Age**: Idade do cliente (entre 16 e 80 anos). As regras se aplicam à idade e ao comportamento de compra.

**State**: Estado nigeriano onde o cliente reside, incluindo o FCT.

**MTN Device**: Dispositivo adquirido pelo cliente. Inclui: Mobile SIM Card, Broadband MiFi, 4G Router, 5G Broadband Router.

**Gender**: Gênero do cliente (Male ou Female).

**Satisfaction Rate**: uma pontuação de 0 a 5 que reflete a satisfação do cliente.

**Customer Review**: Avaliação categórica da experiência do cliente: Poor, Fair, Good, Very Good, Excellent.

**Customer Tenure in months**: há quanto tempo o cliente está inscrito (em meses).

**Subscription Plan**: o nome do plano de dados MTN adquirido.

**Unit Price**: Custo do plano de dados em Naira nigeriana (₦).

**Data Usage**: uso estimado de dados em gigabytes (GB). Não necessariamente igual ao tamanho do plano — reflete o comportamento de uso.

**Number of Times Purchased**: Quantas vezes o plano foi adquirido no mês (simula a taxa de consumo do cliente).

**Total Revenue**: valor total gasto pelo cliente (calculado como preço unitário × número de vezes comprado).

**Customer Churn Status**: indica se o cliente cancelou a compra (Yes) ou ainda está ativo (No).

**Reasons for Churn**: Em caso de rotatividade, este campo mostra o motivo (por exemplo, rede ruim, realocação, tarifas de chamadas altas, etc.). Vazio para clientes ativos.



## 📂 Estrutura do Projeto

* **notebooks/**: Notebook principal com a análise.
* **src/**: Arquivo .py para a obtenção de Dataset.
* **requirements.txt**: Lista de pacotes necessários para execução.


## 🛠️ Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/seuusuario/telecom-customer-analysis-spark.git
```

2. Instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

3. Abra o Jupyter Notebook e execute o arquivo em `notebooks/analise_telecom_spark.ipynb`.

⚠️ **Observação:** É necessário ter o **Java** instalado para rodar o PySpark corretamente.

## 🔥 Principais Análises e Insights

* Quantidade de clientes por tipo de serviço
* Média de satisfação por plano de assinatura
* Análise de ticket médio dos clientes
* Taxa de inatividade por tipo de serviço
* Identificação de planos com maior retenção de clientes
