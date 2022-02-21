import os


class ArquivosTexto:

    def __init__(self):
        self.path = os.getcwd()

    def CreateArch(self, nome):
        """Cria o arquivo txt com o nome do cliente"""
        with open(self.path.join(f'ClientesCadastrados\\{nome.txt}'), 'a') as conta:
            conta.write(f'- Conta de {nome}\n\n')
            conta.close()

    def DeleteArch(self, nome):
        """Deleta o arquivo txt do cliente"""
        os.remove(self.path.join(f'ClientesCadastrados\\{nome.txt}'))

    def WriteAccount(self, nome, anotacoes):
        """Escreve na conta do cliente"""
        with open(self.path.join(f'ClientesCadastrados\\{nome.txt}'), 'w+') as conta:
            conta.write(f'{anotacoes}\n\n')
            conta.close()

    def ReadAccount(self, nome):
        """ Lê o arquivo do cliente e retorna o conteúdo"""
        with open(self.path.join(f'ClientesCadastrados\\{nome.txt}'), 'r') as conta:
            arquivo_da_conta = conta.read()
            conta.close()
            return arquivo_da_conta
