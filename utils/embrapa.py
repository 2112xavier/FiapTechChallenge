import json
import pandas as pd 

class Embrapa:

    def categoria(self, urls):
        if 'Viniferas' in urls:
            return 'Viniferas'
    
        elif 'Americanas' in urls: 
            return 'Americanas e hibridas'
    
        elif 'Mesa' in urls:
            return 'Uvas de mesa'
    
        elif 'ImpVinhos' in urls:
            return 'Vinhos de mesa'
    
        elif 'ImpEspumantes' in urls:
            return 'Espumantes'
    
        elif 'ImpFrescas' in urls:
            return 'Uvas frescas'
    
        elif 'ImpPassas' in urls:
            return 'Uvas passas'
    
        elif 'ImpSuco' in urls:
            return 'Suco de uva'
    
        elif 'ExpVinho' in urls:
            return 'Vinhos de mesa'
    
        elif 'ExpEspumantes' in urls:
            return 'Espumantes'
    
        elif 'ExpUva' in urls:
            return 'Uvas frescas'
    
        elif 'ExpSuco' in urls:
            return 'Suco de uva'    
        
    def producao(self):
        url = 'http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv'
        df = pd.read_csv(url, delimiter=';', encoding='utf-8')   
        return json.loads(df.to_json(orient='records')) 
    
    def processamento(self):
        urls = ["http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
                'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv', 
                'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv']
        dfs = []
        for url in urls:
            df_ = pd.read_csv(url, delimiter='\t', encoding='utf-8')
            df_.insert(1, 'categoria', self.categoria(url))
            dfs.append(df_)
        df = pd.concat(dfs, ignore_index=True)

        return json.loads(df.to_json(orient='records'))    
    
    def comercializacao(self):
        url = "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
        df = pd.read_csv(url, delimiter=';', encoding='utf-8')   
        return json.loads(df.to_json(orient='records'))

    def importacao(self):
        urls = ['http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv', 
                'http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv', 
                'http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv',
                'http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv', 
                'http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv'] 
        dfs = []
        for url in urls:
            df_ = pd.read_csv(url, delimiter=';', encoding='utf-8')
            df_.insert(1, 'categoria', self.categoria(url))
            dfs.append(df_)
        df = pd.concat(dfs, ignore_index=True)
        return json.loads(df.to_json(orient='records'))
    
    def exportacao(self):
        urls = ['http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv', 
                'http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv', 
                'http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv',
                'http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv'] 
        dfs = []
        for url in urls:
            df_ = pd.read_csv(url, delimiter=';', encoding='utf-8')
            df_.insert(1, 'categoria', self.categoria(url))
            dfs.append(df_)
        df = pd.concat(dfs, ignore_index=True)
        return json.loads(df.to_json(orient='records'))
    
