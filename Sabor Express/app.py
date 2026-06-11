import os

def exibir_nome_do_programa():
    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█''')

def exibir_opcoes():
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def encerrar():
    os.system('clear')
    print('Encerrando o programa')

def escolher_opcoes():
    opcao_escolhida = input('Escolha uma opção: ')

    if opcao_escolhida == '1':
        print('Cadastrar Restaurante')
    elif opcao_escolhida == '2':
        print('Listar Restaurantes')
    elif opcao_escolhida == '3':
        print('Ativar Restaurante')
    else: 
        encerrar()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
    