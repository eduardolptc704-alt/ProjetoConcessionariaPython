from Classes.Concessionaria import Concessionaria
from Classes.Agendamento import Agendamento
from Servicos.cadastro import cadastrar_cliente
from Servicos.salvar_dados import salvar_cliente
from Servicos.estoque_inicial import carregar_estoque
from Servicos.login import realizar_login
from Servicos.salvar_agendamento import registrar_e_exibir_agendamento


def main():
    # Inicializa a concessionária e carrega os carros do CSV
    minha_concessionaria = Concessionaria()
    carregar_estoque(minha_concessionaria)

    print("--- Bem-vindo à Concessionária Digital ---")

    # Verificação de Usuário Existente
    cliente = None

    while str(cliente) == "None":  # Roda até que um cliente seja validado ou criado
        ja_e_cliente = input("\nVocê já possui cadastro? (S/N): ").strip().upper()

        if ja_e_cliente == 'S':
            cliente = realizar_login()  # Tenta fazer o login
            if cliente:
                print(f"Bem-vindo de volta, {cliente.nome}!")

        elif ja_e_cliente == 'N':
            cliente = cadastrar_cliente()  # Faz um novo cadastro

            # Se o e-mail digitado já existir, o cadastro retorna None e o loop reinicia
            if not cliente:
                continue

            cliente.exibir_dados()
            salvar_cliente(cliente)
            print("\n--- Cadastro concluído com sucesso e salvo no sistema! ---")
        else:
            print("Opção inválida. Digite S para Sim ou N para Não.")

    # Exibição do estoque movida para fora do loop para aparecer em ambos os casos (Login ou Cadastro)
    print(f"\n--- Modelos disponíveis no pátio ---")
    for carro in minha_concessionaria.estoque:
        print(f"• {carro.marca} {carro.modelo} | Ano: {carro.ano}")
    print("-" * 50)

    while True:
        try:
            orcamento = float(input("\nDigite o valor disponível para compra: R$ "))
        except ValueError:
            print("Por favor, digite apenas números.")
            continue

        carros_disponiveis = minha_concessionaria.buscar_por_orcamento(orcamento)

        if len(carros_disponiveis) == 0:
            print("\nNenhum veículo encontrado para esse orçamento.")
            opcao = input("Deseja aumentar o valor do orçamento? (S/N): ").strip().upper()
            if opcao == 'S':
                continue
            else:
                print(f"\nObrigado por nos visitar, {cliente.nome}! Até logo.")
                return
        else:
            break

    print("\n=== VEÍCULOS DISPONÍVEIS ===\n")
    for indice, carro in enumerate(carros_disponiveis, start=1):
        # Transforma o valor 100000.0 em "100.000,00"
        preco_formatado = f"{carro.preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        print(f"[{indice}] {carro.marca} {carro.modelo}")
        print(f"    Ano: {carro.ano} | Preço: R$ {preco_formatado}")
        print("-" * 50)

    while True:
        try:
            escolha = int(input("\nDigite o número do veículo escolhido: "))
            if 1 <= escolha <= len(carros_disponiveis):
                carro_chosen = carros_disponiveis[escolha - 1]
                break
            else:
                print(f"Escolha inválida. Digite um número entre 1 e {len(carros_disponiveis)}.")
        except ValueError:
            print("Por favor, digite um número inteiro.")

    print(f"\nÓtima escolha! O {carro_chosen.modelo} é um excelente veículo.")
    dia_contato = input("Qual o melhor dia para entrarmos em contato? ")
    horario_contato = input("Qual o melhor horário para entrarmos em contato? ")

    novo_agendamento = Agendamento(cliente, carro_chosen, horario_contato, dia_contato)
    registrar_e_exibir_agendamento(novo_agendamento)

    print("Agradecemos pela preferência!")


if __name__ == "__main__":
    main()
