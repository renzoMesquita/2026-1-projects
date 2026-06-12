import os

def exibir_nome_do_programa():
    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█''')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def encerrar():
    os.system('clear')
    print('Encerrando o programa')

def escolher_opcao():
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == '1':
            print('Cadastrar Restaurante')
        elif opcao_escolhida == '2':
            print('Listar Restaurantes')
        elif opcao_escolhida == '3':
            print('Ativar Restaurante')
        elif opcao_escolhida == '4':
            print('Encerrando programa')
            encerrar()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def opcao_invalida():
    print('Opcao invalida!\n')
    input('Digite uma tecla para voltar: ')
    main()

def cadastrar_novo_restaurante():
        
def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()