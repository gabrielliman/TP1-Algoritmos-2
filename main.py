from sys import argv
import LZ78

def main():
    entrada = argv[2]
    
    if argv[1] == '-c':
        if len(argv) == 5:
            saida = argv[4]
        else:
            saida = entrada[:-3] + 'z78'
        LZ78.comprimir(entrada, saida)
    else:
        if len(argv) == 5:
            saida = argv[4]
        else:
            saida = entrada[:-3] + 'txt'
        LZ78.descomprimir(entrada, saida)


if __name__ == '__main__':
    main()
