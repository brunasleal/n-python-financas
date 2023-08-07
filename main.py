from Utils.cep import valida_cep
from Utils.data import valida_data_nascimento
from Utils.funcoes_auxiliares import formata_texto, retorna_menu_principal
from Utils.valida_cpf import valida_cpf
from Utils.valida_rg import valida_rg

clientes = []

def main():
    validador = True
    while validador:
        print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da N. Selecione uma das opções abaixo:")
        print("1 - Cadastrar cliente")
        print("2 - Cadastrar ação")
        print("3 - Realizar análise da carteira")
        print("4 - Imprimir relatório da carteira")
        print("5 - Sair")

        opcao = input("Digite apena o número da opção desejada: ")

        if opcao == "1":
            print("Informe os dados do cliente: ")
            cliente = {
                "nome": formata_texto(input("Nome: ")),
                "cpf": valida_cpf(),
                "rg": valida_rg(),
                "data_nascimento": valida_data_nascimento(),
                "endereco": valida_cep(),
                "numero_casa": input("Número casa: ")
            }
            clientes.append(cliente)
            print(clientes)
            validador = retorna_menu_principal()

        elif opcao == "2":
            pass
            # Preencher a função da ordem.
        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "5":
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
            validador = False
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    print(main())
