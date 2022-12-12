class Campo_vazio:
    def __init__(self, usuario_digitado, senha_digitada):
        self.setUsuario_digitado(usuario_digitado)
        self.setSenha_digitada(senha_digitada)
    # GET
    def setUsuario_digitado(self,usuario_digitado):
        self.usuario_digitado=usuario_digitado
    def setSenha_digitada(self, senha_digitada):
        self.senha_digitada = senha_digitada
    # SET
    def getUsuario_digitado(self):
        return self.usuario_digitado
    def getSenha_digitada(self):
        return self.senha_digitada

    # CONFERENCIA

    def conferir_usuario_v(self):
        if usuario_digitado != "":
            print('usuario não está <> vazio')
            print('proximo passo é conferir se a senha está vazia')
            Campo_vazio.conferir_senha_v()
            print('passou para conferir se a senha está vazia')
        else:
            return messagebox.showinfo("Jota Contabilidade", "CAMPO USUÁRIO ESTÁ VAZIO")

    def conferir_senha_v(self):
        if senha_digitada != "":
            print('senha não está <> vazio')
            print('passar as informações para conferir se usuario tem no banco de dados')

            print('passou paraa a conferencia do banco de dados')
        else:
            return messagebox.showinfo("Jota Contabilidade", "CAMPO SENHA ESTÁ VAZIO")

campo_vazio=Campo_vazio()
