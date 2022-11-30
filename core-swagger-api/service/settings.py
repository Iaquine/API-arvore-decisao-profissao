import os

"""
    Variaveis booleanas e objetos nao poderao ser definidas nas variaveis de ambiente,
    pois todas serao convertidas para string.
    Para as variaveis definidas com "os.environ.get()" o primeiro valor é referente
    a variavel que está buscando, o segundo valor será usado como valor padrão caso
    não encontre nas variaveis de ambiente.
"""
API_NAME = "Servico API"
VERSION_API = '1.0.1'
TITLE_API = "API - ESCOLHA DE PROFISSAO"
DESCRIPTION_API = " ENFJ-A ou ENFJ-T (Protagonista)'-0 | 'ENFP-A ou ENFP-T (Ativista)'-1 | 'ENTJ-A ou ENTJ-T (Comandante)'-2 | 'ENTP-A ou ENTP-T (Inovador)'-3 | 'ESFJ-A ou ESFJ-T (Cônsul)'-4 | 'ESFP-A ou ESFP-T (Animador)'-5 | \n -=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=- \n 'ESTP-A ou ESTP-T (Empresário)'-6 | 'INFJ-A ou INFJ-T (Advogado)'-7 | 'INFP-A ou INFP-T (Mediador)'-8 | 'INTJ-A ou INTJ-T (Arquiteto)'-9 | 'INTP-A ou INTP-T (Lógico)'-10 | 'ISFJ-A ou ISFJ-T (Defensor)'-11 |\n -=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=- \n 'ISTJ-A ou ISTJ-T (Logístico)'-12 | 'ISTP-A ou ISTP-T (Virtuoso)'-13 \n -=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=- \n Matemática-0 | Português-1 | Artes-2 | Física-3 | Geografia-4 | História-5 | Biologia-6 | Língua estrangeira (ex. Inglês ou Espanhol )-7 | Química-8 | Computação-9 | Geometria-10 | Educação Física-11"

# Flask settings
FLASK_SERVER_NAME = None
FLASK_HOST = os.environ.get('FLASK_HOST', "0.0.0.0")
FLASK_PORT = os.environ.get('FLASK_PORT', "9000")
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

URL_PREFIX = os.environ.get('URL_PREFIX', '')

PATH_LOG = os.environ.get("PATH_LOG", "./log_project_name")
POOL_CPU = int(os.environ.get("POOL_CPU", os.cpu_count()-1))
