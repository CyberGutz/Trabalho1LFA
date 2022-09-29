class AutomatoFD:
    
    def __init__(self, Alfabeto):
        Alfabeto = str(Alfabeto)            
        self.estados = set()
        self.alfabeto = Alfabeto
        self.transicoes = dict()
        self.inicial = None
        self.finais = set()

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

