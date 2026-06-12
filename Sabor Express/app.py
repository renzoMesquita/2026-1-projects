import os

restaurantes = []

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

def opcao_invalida():
    print('Opcao invalida!\n')
    input('Digite uma tecla para voltar: ')
    main()

def cadastrar_novo_restaurante():
    os.system('clear')
    print('Cadastro\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado')
    input('Digite uma tecla para voltar ao menu: ')
    main()

def escolher_opcao():
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar Restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            encerrar()
        else: 
            opcao_invalida()
    except Exception as e:
         print(f'Erro: {e}')
        
def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()