import os

restaurantes = [{'nome' : 'Matuto', 'categoria' : 'Churrasco', 'ativo' : False},
                {'nome' : 'Satoshi', 'categoria' : 'Japonês', 'ativo' : False}]

def exibir_nome_do_programa():
    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█''')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def encerrar():
    exibir_subtitulo('Finalizando app...')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar: ')
    main()

def opcao_invalida():
    print('Opcao invalida!\n')
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome' : nome_do_restaurante, 'categoria' : categoria_restaurante, 'ativo' : False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Restaurantes: ')
    for x in restaurantes:
        nome_restaurante = x['nome']
        categoria_restaurante = x['categoria']
        if x['ativo'] == True:
            restaurante_ativo = 'Restaurante Ativo'
        else:
            restaurante_ativo = 'Restaurante Desativado'
        print(f'.{nome_restaurante} | {categoria_restaurante} | {restaurante_ativo}')
    voltar_ao_menu()

def escolher_opcao():
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            encerrar()
        else: 
            opcao_invalida()
    except Exception as e:
         opcao_invalida()
        
def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()