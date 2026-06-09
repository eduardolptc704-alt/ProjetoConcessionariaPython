class Cliente:

    def __init__(self, nome, email, telefone, endereco, senha):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.__senha = str(senha)

    # Método para exibir os dados na tela
    def exibir_dados(self):
        print("\n=== DADOS DO CLIENTE ===")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

    # GETTER: Permite ler a senha com 'cliente.senha'
    @property
    def senha(self):
        return self.__senha

    # SETTER: Valida a senha ao tentar alterá-la
    @senha.setter
    def senha(self, nova_senha):
        if len(str(nova_senha).strip()) >= 4:
            self.__senha = str(nova_senha).strip()
        else:
            print("❌ Erro de Segurança: A senha deve conter pelo menos 4 dígitos!")