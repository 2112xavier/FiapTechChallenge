"""
uvicorn app:app --reload
"""
from fastapi import FastAPI

from utils.embrapa import Embrapa

embrapa = Embrapa() 

app = FastAPI()

@app.get("/producao")
def read_producao():
    """
    Banco de dados de uva, vinho e derivados. Produção de vinhos, sucos e derivados do Rio Grande do Sul
    """
    return embrapa.producao() 

@app.get("/processamento")
def read_processamento():
    """
    Banco de dados de uva, vinho e derivados. Quantidade de uvas processadas no Rio Grande do Sul
    """
    return embrapa.processamento() 

@app.get("/comercializacao")
def read_comercializacao():
    """
    Banco de dados de uva, vinho e derivados. Comercialização de vinhos e derivados no Rio Grande do Sul
    """
    return embrapa.comercializacao() 

@app.get("/importacao")
def read_importacao():
    """
    Banco de dados de uva, vinho e derivados. Importação de derivados de uva
    """
    return embrapa.importacao() 

@app.get("/exportacao")
def read_exportacao():
    """
    Banco de dados de uva, vinho e derivados. Exportação de derivados de uva
    """
    return embrapa.exportacao() 
