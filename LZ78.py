from trie import Trie

def comprimir(input, output):
    with open(input, 'r') as entrada, open(output, 'wb') as saidabin:
        cadeia=""
        dicionario =Trie()
        vetor=[]
        tam_palavra=0
        while True:
            caractere = entrada.read(1)         
            if (caractere==""):
                break
            if(dicionario.boolpesquisaPalavra(cadeia+caractere)):
                cadeia=cadeia+caractere
            else:
                codigo=dicionario.pesquisaPalavra(cadeia)
                dicionario.inserir(cadeia+caractere)
                cadeia=''
                #colocando a palavra e o codigo em binario e adicionando ao nosso vetor
                palavra= caractere
                tam_palavra = max(tam_palavra, len(format(ord(palavra), '08b')))
                vetor.append((codigo, palavra))



        tam_codigo=dicionario.getMaior_codigo().bit_length()
        tam_codigo=(tam_codigo+7)//8
        tam_palavra=(tam_palavra+7)//8
        bintam_codigo=tam_codigo.to_bytes(1,'big')
        bintam_palavra=tam_palavra.to_bytes(1,'big')

        saidabin.write(bintam_codigo + bintam_palavra)

        for i in range(len(vetor)):
            codigo = vetor[i][0].to_bytes(tam_codigo, "big")
            if(vetor[i][1]!=""):
                palavra = ord(vetor[i][1]).to_bytes(tam_palavra, 'big')
                saidabin.write(codigo+palavra)
            else: saidabin.write(codigo)


def descomprimir(input, output):
    dicionario=Trie()
    raiz=dicionario.getRaiz()
    with open(input, "rb") as entradabin,open(output, "w") as saida:
        tam_codigo = ord(entradabin.read(1))
        tam_palavra = ord(entradabin.read(1))
        while True:
                codigo_bytes = (entradabin.read(tam_codigo))
                if not codigo_bytes:
                    break
                codigo =  int.from_bytes(codigo_bytes, byteorder='big')
                palavra_bytes  = entradabin.read(tam_palavra)
                palavra = bytes(palavra_bytes).decode('latin-1')
                cadeia = dicionario.pesquisaCodigo(raiz, codigo)
                if(palavra != ''):
                    dicionario.inserir(cadeia+palavra)
                    saida.write(cadeia + palavra)
                else:
                    saida.write(cadeia)
