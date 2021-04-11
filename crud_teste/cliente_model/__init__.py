# Classe Cliente_Model conecta ao arquivo csv

"""
A classe Cliente_Model possui os determinados atributos:
    * id
    * nome
    * senha
    * tipo
"""

# Variáveis globais
arquivo = 'cliente.txt'
cabecalho = ("id", "nome", "senha", "tipo")


class Cliente_Model:

    def __init__(self, cliente):
        self.iniciar_arquivo()

        self.id = self.gerar_id(cliente['nome'], cliente['senha'])
        self.nome = cliente['nome']
        self.senha = cliente['senha']
        self.tipo = 1

    def criar_arquivo(self):
        """ Cria o arquivo cliente.txt, que armazena os dados do cliente"""
        try:
            arq = open(arquivo, 'wt+')
            arq.close()
        except:
            print('Houve um ERRO na criação do arquivo')
        else:
            print('Arquivo {} criado com sucesso'.format(arquivo))

    def criar_cabecalho(self):
        """ Cria o cabeçalho do arquivo"""
        try:
            arq = open(arquivo, 'at')
        except:
            print('Houve um ERRO ao escrever o arquivo')
        else:
            try:
                for n, i in enumerate(cabecalho):
                    if n != 3:
                        arq.write('{};'.format(i))
                    else:
                        arq.write('{}'.format(i))
                arq.write('\n')
            except:
                print('Houve um ERRO na hora de escrver o cabeçalho')
            else:
                arq.close()

    def iniciar_arquivo(self):
        try:
            arq = open(arquivo, 'rt')
            arq.close()
        except FileNotFoundError:
            self.criar_arquivo()
            self.criar_cabecalho()

    def modificar_liha(self, linha):
        linha = linha.split("\n")[0]
        linha = linha.split(";")
        return linha

    def login(self, nome, senha):
        """ Encontra a id do cliente pelo nome e pela senha"""
        for linha in self.ler_clientes():
            if linha[1] == nome and linha[2] == senha:
                return linha[0]

    def gerar_id(self, nome, senha):
        """ Gera um id para o cliente"""
        id = self.login(nome, senha)
        if id != None:
            return id
        else:
            key = 0 # chave de verificação
            with open(arquivo, 'r') as arq:
                for linha in arq.readlines():
                    linha = self.modificar_liha(linha)
                    if linha[0] == 'id':
                        key = 1
                        return 1
            if key == 0:
                ultimo_id = self.ler_clientes()[-1][0]
                return int(ultimo_id) + 1

    def escrever(self, nova_linha):
        """ Função auxiliar que ajuda a escrever no arquivo"""
        with open(arquivo, 'w') as arq:
            for linha in nova_linha:
                arq.writelines(linha)

    def criar_cliente(self):
        """ Armazena os dados do cliente dentro do arquivo"""
        dados = {'id': self.id,
                'nome': self.nome,
                'senha': self.senha,
                'tipo': self.tipo}
        try:
            arq = open(arquivo, 'at')
        except:
            print('Houve um ERRO ao escrever no arquivo')
        else:
            try:
                for key, value in dados.items():
                    if key != "tipo":
                       arq.write("{};".format(value))
                    else:
                        arq.write("{}".format(value))
                arq.write("\n")
            except Exception as erro:
                print("Infelismente tivemos um problema no {}".format(erro.__class__))
                print(dados)
            else:
                print('Cliente cadastrado com sucesso')
                arq.close()

    def ler_cliente(self, id):
        """ Procura um determinado cliente por sua id"""
        try:
            arq = open(arquivo, 'rt')
        except:
            print("Não é possível ler o arquivo")
        else:
            try:
                for linha in arq:
                    linha = self.modificar_liha(linha)
                    if linha[0] == id:
                        cliente = linha
            except Exception as erro:
                print("Infelismente tivemos um problema no {}".format(erro.__class__))
            else:
                arq.close()
                return cliente

    def ler_clientes(self):
        """ Lista todos os clientes"""
        lista = []
        try:
            arq = open(arquivo, 'rt')
        except:
            print("Não é possível ler o arquivo")
        else:
            for linha in arq:
                linha = linha.split("\n")[0]
                linha = linha.split(";")
                lista.append(linha)
        arq.close()
        return lista[1:]

    def update_cliente(self, nome, senha):
        """ Atualiza os dados de um determinado cliente"""

        dados = {'id': self.id,
                 'nome': nome,
                 'senha': senha,
                 'tipo': self.tipo}

        with open(arquivo, 'r') as arq:
           nova_linha = []
           for linha in arq.readlines():
               linha = self.modificar_liha(linha)
               if linha[0] == dados['id']:
                    for k, v in dados.items():
                        if k != 'tipo':
                            nova_linha.append("{};".format(v))
                        else:
                            nova_linha.append("{}\n".format(v))
               else:
                   for k, v in enumerate(linha):
                       if k != 3:
                           nova_linha.append("{};".format(v))
                       else:
                           nova_linha.append("{}\n".format(v))

        self.escrever(nova_linha)

    def deletar_cliente(self, id):
        """ Deleta os dados de um determinado cliente"""
        with open(arquivo, 'r') as arq:
            nova_linha = []
            for linha in arq.readlines():
                linha = self.modificar_liha(linha)
                if linha[0] != id:
                    for k, v in enumerate(linha):
                        if k != 3:
                            nova_linha.append("{};".format(v))
                        else:
                            nova_linha.append("{}\n".format(v))

        self.escrever(nova_linha)














