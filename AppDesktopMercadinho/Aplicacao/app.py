from tkinter import *
from placeholder import EntPlaceHold
from gradiente import GradientFrame
from tkinter import ttk, messagebox
from funcoes_sqlite import FuncsSqlite
from funcoes_txt import ArquivosTexto


class Front(FuncsSqlite, ArquivosTexto):

    def __init__(self):
        self.window = Tk()
        self.CreateTable()

    def WindowConfigure(self):
        """
        Faz as configurações inicais da tela e põe a imagem de fundo na Interface
        """
        self.window.geometry("1919x1056")
        self.window.title('Contas')
        self.back_interface = PhotoImage(
            file='C:\\Users\\JR BARBOSA\\Desktop\\tkinterframe\\ProjetoTkinterMerc\\img\\back_interface.png')
        label_interface = Label(self.window, image=self.back_interface)
        label_interface.pack()

    def CreateFrames(self):
        """
        Esse método cria todos os frames da aplicação de uma vez sem definir a posição deles. Tornado mais fácil sua
        manipulação.
        """
        self.frame_cad = GradientFrame(self.window, bd=4, bg='#dfe3ee', highlightbackground='#759fe6',
                                       highlightthickness=2,
                                       color1='#00FF00', color2='#ADFF2F')

        self.frame_del = GradientFrame(self.window, bd=4, bg='#dfe3ee', highlightbackground='#759fe6',
                                       highlightthickness=2,
                                       color1='#FFD700', color2='#FF0000')

        self.frame_lista = GradientFrame(self.window, bd=4, highlightbackground='#759fe6',
                                         highlightthickness=2,
                                         color1='#00BFFF', color2='#1E90FF')

    def WidgetsIniciais(self):
        """
        Cria os botões da Interface Inicial
        """
        # Ícones dos botões da Interface Inicial
        self.img_cadastro = PhotoImage(
            file='C:\\Users\\JR BARBOSA\\Desktop\\tkinterframe\\ProjetoTkinterMerc\\img\\icone_cadastro.png')
        self.img_excluir = PhotoImage(
            file='C:\\Users\\JR BARBOSA\\Desktop\\tkinterframe\\ProjetoTkinterMerc\\img\\icone_deletar.png')
        self.img_conta = PhotoImage(
            file='C:\\Users\\JR BARBOSA\\Desktop\\tkinterframe\\ProjetoTkinterMerc\\img\\icone_conta.png')

        # Label e Botão de cadastro
        self.button_cadastro = Button(self.window, image=self.img_cadastro, cursor='hand2',
                                      command=self.IntCadastro)
        self.button_cadastro.place(relx=0.02, rely=0.07)

        self.label_cadastro = Label(self.window, text='Cadastrar Cliente', font=("Verdana Bold", 12), bg='white')
        self.label_cadastro.place(relx=0.02, rely=0.05)

        # Label e Botão de Exclusão do cliente
        self.button_excluir = Button(self.window, image=self.img_excluir, cursor='hand2', command=self.IntDelete)
        self.button_excluir.place(relx=0.02, rely=0.3)

        self.label_excluir = Label(self.window, text='Deletar Cliente', font=("Verdana Bold", 12), bg='white')
        self.label_excluir.place(relx=0.02, rely=0.28)

        # Label e Botão da conta
        self.button_conta = Button(self.window, image=self.img_conta, cursor='hand2', command=self.IntVerConta)
        self.button_conta.place(relx=0.02, rely=0.53)

        self.label_conta = Label(self.window, text='Ver Conta', font=("Verdana Bold", 12), bg='white')
        self.label_conta.place(relx=0.02, rely=0.51)

    # Essa função limpa os widgets iniciais da interface para prosseguir para outra sessão.

    def LimparWidgetsIniciais(self):
        self.widgtes_principais = [self.button_cadastro, self.button_excluir,
                                   self.button_conta,
                                   self.label_cadastro, self.label_excluir,
                                   self.label_conta]
        for widget in self.widgtes_principais:
            widget.place_forget()

    # Essa função cria os Widgets que serão utilizados na função 'IntCadastro()' que criará a interface de cadastro.

    def WidgetsCadastro(self):
        self.frame_cad.place(relx=0.03, rely=0.1, relwidth=0.3, relheight=0.15)

        # Label e Entry do nome do cliente
        self.label_nome = Label(self.frame_cad, text='Nome', fg='black', bg='#7CFC00')
        self.label_nome.place(relx=0.22, rely=0.4)

        self.entry_nome = EntPlaceHold(self.frame_cad, 'Digite o nome do cliente para cadastrá-lo')
        self.entry_nome.place(relx=0.32, rely=0.4, relwidth=0.5)

        self.btn_cadastro = Button(self.frame_cad, text='Cadastrar', bd=4, command=self.ComandoCadastro)
        self.btn_cadastro.place(relx=0.46, rely=0.6)

    # Essa função cria os Widgets que serão utilizados na função 'IntDelete()' que criará o frame de deletar cliente

    def WidgetsDelete(self):
        self.frame_del.place(relx=0.03, rely=0.1, relwidth=0.3, relheight=0.15)

        self.label_nome_delete = Label(self.frame_del, text='Nome', fg='black', bg='#FFA500')
        self.label_nome_delete.place(relx=0.22, rely=0.4)

        self.entry_nome_del = EntPlaceHold(self.frame_del, 'Digite o nome do cliente para Deletá-lo')
        self.entry_nome_del.place(relx=0.32, rely=0.4, relwidth=0.5)

        self.btn_delete = Button(self.frame_del, text='Deletar', bd=4, command=self.ComandoDelete)
        self.btn_delete.place(relx=0.46, rely=0.6)

    # Essa função cria os widgets relacionados ao botão Ver Conta
    def WidgetsListaVerConta(self):
        """
        Elementos relacionados a sessão Ver Conta
        """

        # imagens
        self.icone_pesquisa = PhotoImage(
            file='C:\\Users\\JR BARBOSA\\Desktop\\tkinterframe\\ProjetoTkinterMerc\\img\\icone_pesquisa.png')
        self.icone_atualizar_conta = PhotoImage(
            file='C:\\Users\\JR BARBOSA\\Desktop\\tkinterframe\\ProjetoTkinterMerc\\img\\icone_att.png')
        self.icone_abrir = PhotoImage(
            file='C:\\Users\\JR BARBOSA\\Desktop\\tkinterframe\\ProjetoTkinterMerc\\img\\icone_abrir.png')

        # Lista onde aparecem os clientes e suas contas.
        self.lista_ver_conta = ttk.Treeview(self.frame_lista, height=3, column='nome')
        self.frame_lista.place(relx=0.28, rely=0.05, relwidth=0.4, relheight=0.9)

        self.entry_buscar_lista = EntPlaceHold(self.frame_lista, 'Digite o nome do cliente')
        self.entry_buscar_lista.place(relx=0.25, rely=0.03, relwidth=0.5)

        self.botao_buscar_lista = Button(self.frame_lista, image=self.icone_pesquisa, command=self.ComandoBuscarCliente)
        self.botao_buscar_lista.place(relx=0.76, rely=0.027)

        self.area_txt = Text(self.frame_lista)
        self.area_txt.place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.37)
        self.area_txt.configure(font=('Courier', 13), bg='#D3D3D3')

        self.botao_abrir_conta = Button(self.frame_lista, image=self.icone_abrir, command=self.InsertArchEntry)
        self.botao_abrir_conta.place(relx=0.812, rely=0.62)

        self.botao_atualizar = Button(self.frame_lista, image=self.icone_atualizar_conta, command=self.CommandAttAcount)
        self.botao_atualizar.place(relx=0.812, rely=0.68)

        self.lista_ver_conta.heading('#0', text='')
        self.lista_ver_conta.heading('#1', text='Clientes')

        self.lista_ver_conta.column('#0', width=1)
        self.lista_ver_conta.column('#1', width=100)

        self.lista_ver_conta.place(relx=0.3, rely=0.07, relwidth=0.4, relheight=0.5)

        self.Scroollista = Scrollbar(self.frame_lista, orient='vertical')
        self.lista_ver_conta.configure(yscroll=self.Scroollista.set)

        self.Scroollista.place(relx=0.67, rely=0.071, relwidth=0.03, relheight=0.499)

        self.SelectLista(self.lista_ver_conta)

        self.lista_ver_conta.bind('<Double-1>', self.SelectDoubleClick)

    # As funções abaixo são os comandos que serão executados ao acionar os botões da interface inicial

    def IntCadastro(self):
        self.LimparWidgetsIniciais()
        self.WidgetsCadastro()

    def IntDelete(self):
        self.LimparWidgetsIniciais()
        self.WidgetsDelete()

    def IntVerConta(self):
        self.LimparWidgetsIniciais()
        self.WidgetsListaVerConta()

    def ComandoCadastro(self):
        """
        Essa função gera o comando que irá cadastrar o cliente no banco de dados.
        """
        nome_cadastro = self.entry_nome.get()

        if nome_cadastro == '' or nome_cadastro == 'Digite o nome do cliente para cadastrá-lo':
            messagebox.showerror('Erro', 'É preciso digitar o nome do cliente para cadastrá-lo')
        else:
            try:
                self.CreateClient(nome_cadastro)
                self.CreateArch(nome_cadastro)
                messagebox.showinfo('Sucesso', 'Cliente Cadastrado com sucesso!')
            except:
                messagebox.showerror('Erro', 'Houve um erro ao cadastrar o cliente')

    def ComandoDelete(self):
        """
        Essa função gera o comando que irá deletar o cliente do banco de dados. Ao apertar o botão.
        """
        nome_delete = self.entry_nome_del.get()

        if nome_delete == '' or nome_delete == 'Digite o nome do cliente para Deletá-lo':
            messagebox.showerror('Erro', 'Digite um nome válido')
        else:
            confirm_delete = messagebox.askyesno('Confirme', 'Você tem certeza que deseja deletar esse cliente?')
            if confirm_delete:
                try:
                    self.DeleteClient(nome_delete)
                    self.DeleteArch(nome_delete)
                    messagebox.showinfo('Sucesso', 'Cliente deletado com sucesso')
                except FileNotFoundError as erro:
                    print(erro)
                    messagebox.showerror('Erro', 'Houve um erro ao deletar o cliente do banco. Verifique se o cliente '
                                                 'já foi excluído do banco de dados')

    def InsertArchEntry(self):
        """ Esta Função insere o conteúdo do arquivo txt na area de texto do tkinter"""
        self.area_txt.delete('1.0', END)

        try:
            nome = self.entry_buscar_lista.get()
            arquivo_read = self.ReadAccount(nome)

            self.area_txt.insert(END, arquivo_read)
        except FileNotFoundError:
            messagebox.showerror('Erro', 'O cliente digitado não está cadastrado na lista')

    def CommandAttAcount(self):
        """ Função que atualiza o conteúdo do arquivo txt"""
        nome_entry = self.entry_buscar_lista.get()

        if nome_entry == '' or nome_entry == 'Digite o nome do cliente':
            messagebox.showerror('Erro', 'Digite um nome válido')
        else:
            confirm_att = messagebox.askyesno('Confirme', 'Você deseja realmente atualizar a conta desta maneira?')

            if confirm_att:
                try:
                    txt_anotacoes = self.area_txt.get('1.0', END)

                    self.WriteAccount(nome_entry, txt_anotacoes)
                    messagebox.showinfo('Sucesso', 'Conta atualizada com sucesso!')
                except FileNotFoundError as erro:
                    print(erro)
                    messagebox.showerror('Erro', 'O cliente selecionado não está cadastrado. Verifique se o nome está '
                                                 'esxrito exatamente igual como está na lista!')

    def ComandoBuscarCliente(self):
        """ Comando que seleciona o cliente na lista ao buscar ele"""
        self.BuscarCliente(self.lista_ver_conta, self.entry_buscar_lista)

    def Menu(self):
        """
        Menu do topo da tela
        """
        self.barra_menu = Menu(self.window)
        self.window.config(menu=self.barra_menu)
        self.menu_volta = Menu(self.barra_menu)

        self.barra_menu.add_cascade(label='Menu', menu=self.menu_volta)

        self.menu_volta.add_command(label='Voltar', command=self.BackMenu)

    def SelectDoubleClick(self, event):
        """Função que insere o nome do cliente dentro da entry de busca ao dar um duplo clique no nome do cliente"""
        self.entry_buscar_lista.delete(0, END)
        self.lista_ver_conta.selection()

        for nome in self.lista_ver_conta.selection():
            nome_ins = self.lista_ver_conta.item(nome, 'values')
            for n in nome_ins:
                self.entry_buscar_lista.insert(END, n)

    def BackMenu(self):
        """
        Comando que retorna para a interface Inicial a partir de qualquer sessão
        """

        if self.frame_cad:
            self.frame_cad.place_forget()

        if self.frame_del:
            self.frame_del.place_forget()

        if self.frame_lista:
            self.frame_lista.place_forget()

        self.WidgetsIniciais()

    def Iniciar(self):
        """
        Método que inicia a aplicação
        """
        self.WindowConfigure()
        self.CreateFrames()
        self.WidgetsIniciais()
        self.Menu()
        self.window.mainloop()


app = Front()
app.Iniciar()
