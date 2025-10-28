alunoslista = []

def exibir_menu():
    #Exibe o menu de opções para o usuário
    print("Sistema de Gerenciamento de Alunos")
    print("1. Adicionar aluno")
    print("2. Ver alunos")
    print("3. Sair")

def adicionar_aluno():
    # Adiciona um novo aluno e sua nota na lista
    nome = input("Digite o nome do aluno: ")
    print(f"Aluno {nome} adicionado com sucesso!\n")
    try:
        for i in range(3):
            nota = float(input(f"Digite a nota de {nome}: "))
            alunoslista.append(nota)
    except ValueError:
        print("Entrada de nota inválida. Por favor, digite um número.\n")

def ver_alunos():
    # Exibe a lista de todos os alunos e suas notas
    if not alunoslista:
        print("Nenhum aluno cadastrado.\n")
    else:
        print("\n--- Lista de Alunos ---")
        dicio = {
            aluno : nome
        }
        print("---------------------\n")

def main():
    #Função principal que executa o sistema
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_aluno()
        elif escolha == '2':
            ver_alunos()
        elif escolha == '3':
            print("Encerrando o sistema...")
            break  # Interrompe o loop while e finaliza o programa
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.\n")
            
main()