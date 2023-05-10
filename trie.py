class TrieNode:
    def __init__(self, _caractere: str,_codigo = 0):
        self.codigo=_codigo
        self.caractere = _caractere
        self.filhos = {}
        self.fimdepalavra = False


class Trie:
    def __init__(self):
        self.raiz = self.novoNode("")
        self.maior_codigo=0
    
    def novoNode(self, caractere):
        return TrieNode(caractere)

    def getMaior_codigo(self):
        return self.maior_codigo

    def getRaiz(self):
        return(self.raiz)

    def inserir(self, palavra):
        nodo_atual = self.raiz
        tamanho = len(palavra)
        for level in range(tamanho):
            transicao = (palavra[level])
            # se a transição nao leva a nenhum dos filhos
            if not (transicao in nodo_atual.filhos):
                #cria novo filho
                nodo_atual.filhos[transicao] = self.novoNode(transicao)
            #continua a percorrer a partir do filho
            # codigo=nodo_atual.codigo
            nodo_atual = nodo_atual.filhos[transicao]
 
        # adiciono um ao numero de palavras armazenadas pelo nodo e guardo nele o seu codigo
        self.maior_codigo+=1
        nodo_atual.codigo=self.maior_codigo
        nodo_atual.caractere=transicao
        nodo_atual.fimdepalavra = True
        # return codigo

    def boolpesquisaPalavra(self, palavra):
        # busca uma palavra na trie e retorna verdadeiro se ela estiver presente
        nodo_atual = self.raiz
        tamanho = len(palavra)
        for level in range(tamanho):
            transicao = palavra[level]
            if not (transicao in nodo_atual.filhos):
                return False
            nodo_atual = nodo_atual.filhos[transicao]
 
        return nodo_atual.fimdepalavra

    def pesquisaPalavra(self, palavra):
        # busca uma palavra na trie e retorna verdadeiro se ela estiver presente
        if(palavra==""):
            return 0
        nodo_atual = self.raiz
        tamanho = len(palavra)
        for level in range(tamanho):
            transicao = palavra[level]
            if not (transicao in nodo_atual.filhos):
                return False
            nodo_atual = nodo_atual.filhos[transicao]
 
        if(nodo_atual.fimdepalavra):
            return nodo_atual.codigo
        else:
            return False

    
    def pesquisaCodigo(self, nodo_atual: TrieNode, codigo: int, cadeia = ""):
        #busca recursivamente por um nodo com o codigo
        #se o codigo for maior q o maximo n precisa buscar
        if(codigo> self.maior_codigo):
            return ""
        #se achar retorna a palavra
        if(nodo_atual.codigo == codigo):
            return cadeia + nodo_atual.caractere
        #se o nodo nao tiver filhos retorna vazio
        if(len(nodo_atual.filhos) == 0):
            return ""     
        else:
            for filho in nodo_atual.filhos:
                busca_recursiva = self.pesquisaCodigo(nodo_atual.filhos[filho], codigo, (cadeia + nodo_atual.caractere))
                if (busca_recursiva != ""):
                    return busca_recursiva
        return ""


