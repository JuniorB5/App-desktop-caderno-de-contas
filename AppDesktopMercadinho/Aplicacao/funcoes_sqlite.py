import sqlite3
from tkinter import messagebox, END


class FuncsSqlite:
    """
    Classe que possui todas as funcionalidades referentes as ações do banco de dados.
    """

    def Conection(self):
        try:
            self.conection = sqlite3.connect('clientes.db')
            self.cursor = self.conection.cursor()
        except:
            print('ERRO AO CONECTAR AO BANCO DE DADOS')

    def CloseConection(self):
        self.conection.commit()
        self.conection.close()

    def CreateTable(self):
        """
        Criar Tabela: Cria a tabela que guardará todos os dados do cliente. Caso ela ainda não exista no arquivo.
        """
        self.Conection()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS Clientes (
            nome VARCHAR(50) NOT NULL
        );""")
        self.CloseConection()

    def CreateClient(self, nome):
        """
        Criar Cliente: Cria o uma coluna para o cliente no banco de dados.
        """
        self.Conection()

        self.cursor.execute(f"""INSERT INTO Clientes VALUES ('{nome}')""")

        self.CloseConection()

    def DeleteClient(self, nome):
        """
        Deletar Cliente: Deleta Os registros do cliente, segundo o nome dele, no banco de dados.

        """
        self.Conection()

        nome_verificado = self.VerifyAccount(nome)

        if nome_verificado:
            self.cursor.execute(f"""DELETE FROM Clientes WHERE nome = '{nome_verificado}'""")
        else:
            messagebox.showerror('Erro', 'O Cliente não está cadastrado no banco de dados')

        self.CloseConection()

    def SelectLista(self, lista):
        """
        Selecionar Lista: Insere os valores que estão no banco de dados dentro das listas da interface de maneira
        organizada.

        """
        self.Conection()

        self.cursor.execute(f"""SELECT * FROM Clientes ORDER BY nome ASC;""")

        dados = self.cursor.fetchall()

        for dado in dados:
            lista.insert('', END, values=dado)

        self.CloseConection()

    def BuscarCliente(self, lista, entry_nome):
        """
        Buscar Cliente: Essa função busca o cliente no banco de dados segundo a digitação do cliente na entry.
        """
        self.Conection()
        lista.delete(*lista.get_children())

        entry_nome.insert(END, '%')

        nome = entry_nome.get()

        self.cursor.execute(
            f""" SELECT nome FROM clientes WHERE nome LIKE '%s' ORDER BY nome ASC """ % nome)
        nome_busca = self.cursor.fetchall()

        for n in nome_busca:
            lista.insert("", END, values=n)

        entry_nome.delete(0, END)

        self.CloseConection()

    def VerifyAccount(self, nome):
        """
        Verifica Conta: Essa função verifica se o nome digitado nas entrys está cadastrado no banco de dados.
        """
        self.Conection()
        self.cursor.execute(f"""SELECT nome FROM Clientes""")

        nomes = self.cursor.fetchall()

        for name in nomes:
            for n in name:
                if nome in n:
                    return nome

        self.CloseConection()
