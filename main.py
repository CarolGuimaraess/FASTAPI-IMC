from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Pessoa(BaseModel):
    altura: float
    peso: float

@app.get("/")
def pagina_inicial():
    return {"detail": "Acesse o endpoint POST /calcular_imc para calcular o imc"}

# Função para classificar o IMC
def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Acima do peso"
    else:
        return "Obeso"

@app.post("/calcular_imc/")
async def calcular_imc(pessoa: Pessoa):
    altura = pessoa.altura
    peso = pessoa.peso

    if altura <= 0 or peso <= 0:
        raise HTTPException(status_code=400, detail="Altura e peso devem ser valores positivos.")

    imc = peso / (altura ** 2)
    classificacao = classificar_imc(imc)
    return {"IMC": imc, "Classificacao": classificacao}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
