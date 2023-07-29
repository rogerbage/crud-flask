# -*- encoding: utf-8 -*-

from apps.home import blueprint
from apps import api
from flask_restx import Resource
from apps.home.empresas import empresalib


empresaModel = empresalib.getEmpresaModel()
sortModel = empresalib.getSortModel()
updateModel = empresalib.getUpdateModel()

#################################################################################
@api.route('/api')
class RootApi(Resource):

    #########################################
    @api.doc(description="Teste de coneção.")

    def get(self):
        response = {
            "type": "success",
            "message": "connected",
            "info": "API para cadastro de empresas, construída por Roger Morais Borges para a eStracta."
        }
        return (response)    
    ##########################################

#################################################################################




#####################################################################################
@api.route('/api/empresa')
class EmpresaApi(Resource):
    
    ##########################################    
    @api.doc(parser=sortModel)
    @api.doc(description="Listagem das empresas. Com paginação e ordenação.")
    @api.response(200, 'Sucesso.')

    def get(self):
        data = sortModel.parse_args()
        return empresalib.getEmpresas(data)
    #############################################
    

    ###########################################
    @api.doc(parser=empresaModel)
    @api.doc(description="Salve novas empresas no base de dados. ")
    @api.response(400, 'Campos obrigatórios vazios ou CNPJ inválido.')
    @api.response(409, 'CNPJ ou "nome_razao" já existem.')
    @api.response(201, 'Empresa adicionada com sucesso.')
    @api.response(500, 'Erro interno no servidor.')

    def post(self):
        data = empresaModel.parse_args()
        return empresalib.postEmpresa(data)
    ################################################

##########################################################################################





####################################################################################
@api.route('/api/empresa/cnpj/<string:cnpj>')
class EmpresaCnpj(Resource):
    
    ###########################################
    @api.doc(description="Delete uma empresa pelo CNPJ. Aceita apenas caracteres numéricos. ex.: 11111111111111 ;")
    @api.response(400, 'CNPJ Inválido')
    @api.response(404, 'CNPJ não encontrado')
    @api.response(200, 'Empresa deletada com sucesso.')
    @api.response(200, 'Erro interno no servidor.')

    def delete(self, cnpj):
        return empresalib.deleteEmpresaByCnpj(cnpj)
    ############################################

######################################################################################
        




#########################################################################################
@api.route('/api/empresa/id/<int:id>')
class EmpresaById(Resource):

    #########################################
    @api.response(404, 'Id não encontrado.')
    @api.response(200, 'Empresa Encontrada.')
    @api.doc(description="Lista empresa se houver com o id fornecido.")

    def get(self, id):
        return empresalib.getEmpresa(id)
    #########################################        

    #########################################
    @api.doc(description="Atualiza dados da empresa. Permite atualizar apenas 'nome_fantasia' e 'cnae'. Outros campos serão ignorados.")
    @api.doc(parser=updateModel)
    @api.response(400, 'Campos obrigatórios vazios ou inválidos.')
    @api.response(404, 'Id não encontrado.')
    @api.response(200, 'Empresa atualizada com sucesso.')
    @api.response(500, 'Erro interno no servidor.')

    def put(self, id):
        data = updateModel.parse_args()
        return empresalib.putEmpresa(id, data)
    ###########################################
        
    ############################################
    @api.doc(description="Delete uma empresa através do Id.")
    @api.response(404, 'Id não encontrado.')
    @api.response(200, 'Empresa deletada com sucesso.')
    @api.response(500, 'Erro interno no servidor.')

    def delete(self, id):
        return empresalib.deleteEmpresaById(id)
    ##############################################

#######################################################################################        

