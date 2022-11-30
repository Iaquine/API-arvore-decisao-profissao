from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'personalidade': fields.List(fields.Float(), required=True, description="Tipo de Personalidade"),
    'favorita': fields.List(fields.Float(), required=True, description="Disciplina favorita"),
    'odiada': fields.List(fields.Float(), required=True, description="Disciplina que nao gosta")
    })
