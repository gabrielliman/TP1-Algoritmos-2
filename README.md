# TP1-Algoritmos-2
Implementação do algoritmo LZ78, com o uso de uma trie para armazenar o dicionário, para compressão e descompressão de arquivos de texto
# Intruções de uso
Os métodos de compressão e descompressão são utilizados por meio da linha de comando da seguinte forma:
  Compressão: ./main.py -c <arquivo_entrada> [-o <arquivo_saida>]
  Descompressão: ./main.py -x <arquivo_entrada> [-o <arquivo_saida>]
#Trie
Cada nodo da trie armazena um caractere, o código correspondente ao nodo, se ele é o fim de uma cadeia e a referência aos nodos filhos.

A trie é tradicional e possui métodos para inserir novos elementos e pesquisar elementos existentes utilizando os códigos ou utilizando cadeias de caracteres.

**Inserir**
  - Adiciona uma cadeia a trie, criando os nodos necessários nesse processoe não retornando nada

**PesquisaPalavra**
  - Identifica se uma cadeia está presente na trie e caso esteja retorna seu codigo, caso contrario retorna False
 
**PesquisaCodigo**
  - Identifica se um código está presente na trie, retornando a cadeia correspondente ao nodo que possui esse código
 
# Comprimir
 Utiliza o algoritmo padrão LZ78, buscando cadeias que ainda não estejam presentes e as adicionando a árvore, com a adição de armazenar o tamanho maximo em bytes necessario para armazenar uma cadeia e um codigo. Com essa informação, esse dois dados são escritos no header do arquivo comprimido e a saida do LZ78 é escrita em binário com o número de bytes definido anteriormente
 
 # Descomprimir
  Para descomprimir é lido primeiro o header para se ter a informação do tamanho das sequências que representam os codigos e o tamanho das que representam as cadeias. Com isso, todo o arquivo binário é decodificado e se aplica o inverso da LZ78, inserindo cadeias na trie e escrevendo no arquivo de saída conforme a necessidade
  
 # Taxa de Compressão
 Arquivo	Tamanho arquivo original	Tamanho arquivo comprimido	Taxa de compressão
| Arquivo	| Tamanho arquivo original | Tamanho arquivo comprimido |	Taxa de compressão |
|---|---|---|---|
| RomeueJulieta	| 160kb | 129kb |	19,37% |
| aids	| 55kb | 53kb |	3,63% |
| how	| 37kb | 26kb |	29,70% |
| frankestein	| 431kb | 378kb |	19,37% |
| abril	| 456kb | 383kb |	16,00% |
| lusiadas	| 337kb | 189kb |	43,91% |
| mobydcik	| 922kb | 768kb |	16,70% |
| peterpan	| 276kb | 200kb |	27,53% |
| twocities	| 773kb | 630kb |	18,50% |
| warandpeace	| 3217kb | 2210kb |	31,30% |
