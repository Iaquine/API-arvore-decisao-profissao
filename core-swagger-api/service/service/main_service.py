from imp import load_module
from pyexpat import model
import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import pickle as pck

class shows():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_model()

    def load_model(self):
        """"
        Carrega o modelo de classificacão de profissoes
        """
        
        filename = '/code/arvore_model2.pkl'
        self.model = pck.load(open(filename, 'rb'))
        logger.debug(mensagens.FIM_LOAD_MODEL)


    def executar_rest(self, band_scores):
        response = {}

        logger.debug(mensagens.INICIO_PREDICT)
        start_time = time.time()

        response_predicts = self.buscar_predicao(band_scores)

        logger.debug(mensagens.FIM_PREDICT)
        logger.debug(f"Fim de todas as predições em {time.time()-start_time}")
        
        df_response = pd.DataFrame(band_scores, columns=['personalidade','favorita','odiada'])
        df_response['Uma boa profissão para você é:'] = response_predicts
        df_response = df_response.drop(columns=['personalidade','favorita','odiada'])

        response = {"Classificação": json.loads(df_response.to_json(orient='records', force_ascii=False))}

        return response

    def buscar_predicao(self, band_scores):
        """
        Pega o modelo carregado e aplica em texts
        """
        logger.debug('Iniciando o predict...')

        personalidade = float(band_scores['personalidade'][0])
        favorita = float(band_scores['favorita'][0])
        odiada = float(band_scores['odiada'][0])

        dados = [[personalidade,favorita,odiada]]

        self.load_model()
        #model.compile()
        predicted = self.model.predict(dados)
        predicted = int(predicted)
        #print(predicted)
        logger.debug(predicted)
        switcher = {0:'Administração', 1:'Bacharelado em Tecnologia da Informação', 2:'Biotecnologia', 3:'Ciência da Computação',4:'Comunicação Visual, Assistente de Administração, Informática, web Design ', 5:'Contabilidade',6:'Design',7:'Direito',8:'Economia',9:'Educação Física',10:'Enfermagem',11:'Engenharia',12:'Engenharia Civil',13:'Engenharia de Computação',14:'Engenharia de Software',15:'Farmacia',16:'Gastronomia',17:'Gestão de RH',18:'Gestão de Tecnologia da Informação',19:'Gestão de recursos humanos',20:'Hardware',21:'Letras',22:'Medicina',23:'Nutrição',24:'Pedagogia',25:'Programação'}
        predicao = switcher.get(predicted)

        retorno = print(f'Uma boa profissão para você é: {predicao}')
        logger.debug(retorno)

        return predicao