from operator import truediv


class AutomatoFD:
    
    # CRIA O AUTOMATO VAZIO
    def __init__(self, Alfabeto):
        Alfabeto = str(Alfabeto)            
        self.estados = set()
        self.alfabeto = Alfabeto
        self.transicoes = dict()
        self.inicial = None
        self.finais = set()

    #LIMPA O AUTOMATO
    def limpaAfd(self):
        """Inicializa variáveis utilizadas no processamento de cadeias."""
        self.__deuErro = False
        self.__estadoAtual = self.inicial


    def criaEstado(self, id, inicial = False, final = False):
        id = int(id)
        if id in self.estados:
            return False
        
        self.estados = self.estados.union({id})

        if inicial:
            self.inicial = id
        if final:
            self.finais = self.finais.union({id})

        return True

    def criaTransicao(self, origem, destino, simbolo):
        origem = int(origem)
        destino = int(destino)
        simbolo = str(simbolo)

        if not origem in self.estados:
            return False
        if not destino in self.estados:
            return False

        self.transicoes[(origem, simbolo)] = destino
        return True

    
    def mudaEstadoInicial(self, id):
        if not id in self.estados:
            return
        
        self.inicial = id

    
    def mudaEstadoFinal(self, id, final):
        if not id in self.estados:
            return
        
        if final:
            self.finais = self.finais.union({id})
        else:
            self.finais = self.finais.difference({id})


    def move(self, cadeia):
        for simbolo in cadeia:
            if not simbolo in self.alfabeto:
                self.__deuErro = True
                break
            if(self.__estadoAtual, simbolo) in self.transicoes.keys():
                novoEstado = self.transicoes[(self.__estadoAtual, simbolo)]
                self.__estadoAtual = novoEstado
            else:
                self.__deuErro = True
                break

        return self.__estadoAtual


    def deuErro(self):
        return self.__deuErro


    def estadoAtual(self):
        return self.__estadoAtual


    def estadoFinal(self, id):
        return id in self.finais


    def afdToS(self):
        s = 'AFD(E, A, T, i, F): \n'

        s += '  E = { '
        for e in self.estados:
            s += '{}, '.format(str(e))
        s += '}\n'

        s += '  A = { '
        for a in self.alfabeto:
            s += '{}, '.format(a)
        s += '}\n'

        s += '  T = { '
        for (e,a) in self.transicoes:
            d = self.transicoes[(e, a)]
            s += "({}, '{}') -> {} ".format(e, a, d)
        s += '}\n'

        s += '  i = {}'.format(self.inicial)

        s += '  F = { '
        for e in self.finais:
            s += '{}, '.format(str(e))
        s += '}'

        return s

    
    def afdToTxt(self):
        s = self.afdToS

        fname = input("Digite o nome do arquivo (com .txt no final)")

        try:
            saida = open(fname, "w")
            saida.write(s)
            return True
        except:
            print("Não foi possível escrever o autômato no arquivo")
            return False


    def txtToAfd(self):
        fname = input("Digite o nome do arquivo (com .txt no final)")

        try:
            entrada = open(fname);
            return True
        except:
            print("Não foi possível ler o arquivo")

        
    




        
        

