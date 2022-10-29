from ClassesAFD import Util as ut


class AutomatoFD:
    # CRIA O AUTOMATO VAZIO
    def __init__(self, Alfabeto):
        Alfabeto = str(Alfabeto)            
        self.estados = set()
        self.alfabeto = Alfabeto
        self.transicoes = dict()
        self.inicial = None
        self.finais = set()


    # LIMPA O AUTÔMATO
    def limpaAfd(self):
        """Inicializa variáveis utilizadas no processamento de cadeias."""
        self.__deuErro = False
        self.__estadoAtual = self.inicial


    # CRIA UM ESTADO DO AUTÔMATO
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


    # CRIA UMA TRANSIÇÃO
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


    # DEFINE O ESTADO INICIAL
    def mudaEstadoInicial(self, id):
        if not id in self.estados:
            return
        
        self.inicial = id


    # DEFINE O ESTADO FINAL
    def mudaEstadoFinal(self, id, final):
        if not id in self.estados:
            return
        
        if final:
            self.finais = self.finais.union({id})
        else:
            self.finais = self.finais.difference({id})


    # ANDA PELA CADEIA
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


    # RETORNA SE DEU ERRO
    def deuErro(self):
        return self.__deuErro


    # RETORNA O ESTADO ATUAL
    def estadoAtual(self):
        return self.__estadoAtual


    # RETORNA O ESTADO FINAL
    def estadoFinal(self, id):
        return id in self.finais


    # SEMPRE QUE O AUTÔMATO FOR REPRESENTADO EM FORMA DE STRING, ELE VAI USAR ESSA REPRESENTAÇÃO
    def __str__(self):
        s = '\n\nAFD(E, A, T, i, F): \n'

        s += 'E = { '
        for e in self.estados:
            s += '{}, '.format(str(e))
        s += '}\n'

        s += 'A = { '
        for a in self.alfabeto:
            s += '{}, '.format(a)
        s += '}\n'

        s += 'T={'
        for (e,a) in self.transicoes:
            d = self.transicoes[(e, a)]
            s += " ({}, '{}'): {}, ".format(e, a, d)
        s += '}\n'

        s += 'i = {}'.format(self.inicial)

        s += '  F = { '
        for e in self.finais:
            s += '{}, '.format(str(e))
        s += '}\n\n'
        return s

    
    # SALVA O AFD EM UM ARQUIVO TEXTO
    def afdToTxt(self):
        s = str(self)
        fname = input("Digite o nome do arquivo: ")
        fname = fname + ".txt"

        try:
            saida = open(fname, "w")
            saida.write(s)
            return True
        except:
            print("Não foi possível escrever o autômato no arquivo")
            return False


    # CARREGA O AFD DE UM ARQUIVO TEXTO
    def txtToAfd(self):
        fname = input("Digite o nome do arquivo: ")
        fname = fname + ".txt"

        try:
            entrada = open(fname)
            frase = entrada.read()
        except:
            print("Não foi possível ler o arquivo")
            return False

        toremove = "{ },=AEFT()':"

        chaveF = frase.find('}')
        eChave = frase.find('E = {')
        estados = frase[eChave:chaveF]
        estados = ut.char_remove(estados, toremove)

        chaveF = frase.find('}', chaveF+1)
        aChave = frase.find('A = {')
        alfabeto = frase[aChave:chaveF]
        alfabeto = ut.char_remove(alfabeto, toremove)

        chaveF = frase.find('}', chaveF+1)
        tChave = frase.find('T={')
        transicoes = frase[tChave:chaveF]
        transicoes = ut.char_remove(transicoes, toremove)

        iChave = frase.find('i =')
        inicial = frase[iChave+4]

        chaveF = frase.find('}', chaveF+1)
        fChave = frase.find('F = {')
        finais = frase[fChave:chaveF]
        finais = ut.char_remove(finais, toremove)
    
        novoAf = AutomatoFD(alfabeto)
        novoAf.estados = estados
        i=0
        while i < len(transicoes):
            origem = transicoes[i]
            simbolo = transicoes[i+1]
            destino = transicoes[i+2]
            novoAf.transicoes[(origem, simbolo)] = destino
            i = i+3
        novoAf.finais = finais
        novoAf.inicial = inicial

        print("\n\nO autômato carregado foi: ")
        print(novoAf)
        return novoAf


    # COPIA UM AFD PARA OUTRO. NA VERDADE ESSA FUNÇÃO PODE SER USADA PRA COPIAR QUALQUER COISA, VISTO QUE O PYTHON TEM TIPAGEM DINÂMICA
    def copiaAfd(afd):
            copia = afd;
            return copia;



   
    

        
    




        
        

