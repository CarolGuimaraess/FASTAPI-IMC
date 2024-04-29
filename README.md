# FASTAPI-IMC

# API de Cálculo de IMC (Índice de Massa Corporal)
Esta é uma API simples para calcular o Índice de Massa Corporal (IMC) de uma pessoa com base em sua altura e peso. 

A API utiliza o framework FastAPI em Python.

# Instalação
Após ter dado git clone no projeto, para executar, você precisará do Python instalado em seu sistema. 

Em seguida, instale as dependências usando o pip:
- pip install fastapi uvicorn

# Para iniciar o servidor da API, execute o seguinte comando:
- uvicorn main:app --reload

Isso iniciará o servidor na porta padrão 8000. 
Você pode acessar a documentação interativa da API em http://127.0.0.1:8000/docs.

# Endpoints
- GET /
Este endpoint retorna uma mensagem de boas-vindas com instruções sobre como usar a API.

- POST /calcular_imc/
Este endpoint calcula o IMC com base nos dados fornecidos. Ele espera um corpo JSON com os campos "altura" (em metros) e "peso" (em quilogramas). Se os dados fornecidos não estiverem no formato correto ou forem inválidos (por exemplo, altura ou peso negativos), a API retornará um erro 400 (Bad Request).

O resultado do cálculo é retornado como um JSON contendo o valor do IMC e uma classificação indicando se a pessoa está abaixo do peso, dentro do peso normal, acima do peso ou obesa.
