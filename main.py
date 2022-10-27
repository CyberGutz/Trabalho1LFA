from ClassesAFD import AutomatoFD as af

if __name__ == "__main__":
    afd = af.AutomatoFD('a,b')

    for i in range(1,3):
        afd.criaEstado(i)
    
    afd.mudaEstadoInicial(1)
    afd.mudaEstadoFinal(2,True)

    afd.criaTransicao(1, 2, 'a')
    afd.criaTransicao(2, 1, 'a')
    afd.criaTransicao(2, 2, 'a')
    afd.criaTransicao(1, 1, 'b')
    afd.criaTransicao(2, 1, 'b')

    print(afd)

    afd.afdToTxt()
