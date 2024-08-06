def menu():
    alunos = {}

    def listar_alunos():
        """Listar todos os alunos cadastrados."""
        if alunos:
            for matricula, dados in alunos.items():
                print(f"\nMatrícula: {matricula} \nNome: {dados['nome']} \nIdade: {dados['idade']}")
        else:
            print("\nNenhum aluno cadastrado.")

    def adicionar_aluno():
        """Adicionar um novo aluno."""
        matricula = input("\nDigite a matrícula do aluno: ")
        nome = input("Digite o nome do aluno: ")
        try:
            idade = int(input("Digite a idade do aluno: "))
            if idade < 0:
                raise ValueError
        except ValueError:
            print("\nErro: Idade inválida. A idade deve ser um número positivo.")
            return
        
        if matricula and nome:
            alunos[matricula] = {'nome': nome, 'idade': idade}
            print(f"\nAluno {nome} adicionado com sucesso.")
        else:
            print("\nErro: Dados incompletos para adicionar aluno.")

    def remover_aluno():
        """Remover um aluno existente."""
        matricula = input("\nDigite a matrícula do aluno para remover: ")
        
        if matricula in alunos:
            del alunos[matricula]
            print(f"\nAluno com matrícula {matricula} removido com sucesso.")
        else:
            print("\nErro: Aluno não encontrado ou matrícula não fornecida.")

    def atualizar_idade():
        """Atualizar a idade de um aluno."""
        matricula = input("\nDigite a matrícula do aluno: ")
        try:
            nova_idade = int(input("Digite a nova idade do aluno: "))
            if nova_idade < 0:
                raise ValueError
        except ValueError:
            print("\nErro: Idade inválida. A idade deve ser um número positivo.")
            return
        
        if matricula in alunos:
            alunos[matricula]['idade'] = nova_idade
            print(f"\nIdade do aluno com matrícula {matricula} atualizada para {nova_idade}.")
        else:
            print("\nErro: Aluno não encontrado ou idade não fornecida.")

    def sair():
        """Sair do programa."""
        print("Saindo do programa...")
        exit()

    def first():
        """Função para a primeira opção do menu: Listar alunos"""
        listar_alunos()

    def second():
        """Função para a segunda opção do menu: Adicionar aluno"""
        adicionar_aluno()

    def third():
        """Função para a terceira opção do menu: Remover aluno"""
        remover_aluno()

    def fourth():
        """Função para a quarta opção do menu: Atualizar idade de um aluno"""
        atualizar_idade()

    def fifth():
        """Função para a quinta opção do menu: Sair do programa"""
        sair()

    # Dicionário para mapear opções a funções numeradas
    opcoes = {
        '1': first,
        '2': second,
        '3': third,
        '4': fourth,
        '5': fifth
    }

    while True:
        print("\nMenu:")
        print("1. Listar alunos")
        print("2. Adicionar aluno")
        print("3. Remover aluno")
        print("4. Atualizar idade de um aluno")
        print("5. Sair")

        opcao = input("\nEscolha uma opção (1-5): ")
        
        # Obtém a função correspondente à opção escolhida e a executa
        funcao = opcoes.get(opcao)
        if funcao:
            if funcao():
                break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
