
alunos = [
    {
        "matricula": 1,
        "nome": "João",
        "idade": 15,
        "turma": "A",
        "notas": {
            "matematica": 8.5,
            "portugues": 7.0, }
    },
    {
        "matricula": 2,
        "nome": "Maria",
        "idade": 16,
        "turma": "B",
        "notas": {
            "matematica": 9.0,
            "portugues": 8.5, }
    },
    {
        "matricula": 3,
        "nome": "Pedro",
        "idade": 15,
        "turma": "A",
        "notas": {
            "matematica": 7.5,
            "portugues": 6.0, }
    },
    {
        "matricula": 4,
        "nome": "Ana",
        "idade": 16,
        "turma": "B",
        "notas": {
            "matematica": 8.0,
            "portugues": 9.0, }
    },
]

while True:

    print ("=================================")
    print ("      CADASTRO DE ALUNOS")
    print ("=================================\n")

    print("MENU\n")
    print("1- Cadastro de alunos")
    print("2- listar alunos")
    print("3- buscar alunos")
    print("4- inserir notas")
    print("5- excluir aluno")

    menu = int(input("\nOpção: "))

    if menu == 1:

        while True: 

            print("=====CADASTRO DE ALUNO=====")

            matricula = int(input("Digite a matrícula: "))
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            turma = input("Digite a turma: ")
        
            matematica = float(input("Digite a nota de Matemática: "))
            portugues = float(input("Digite a nota de Português: "))

            aluno = {
                "matricula": matricula,
                "nome": nome,
                "idade": idade,
                "turma": turma,
                "notas": {
                    "matematica": matematica,
                    "portugues": portugues
                }
            }
            alunos.append(aluno)

            print("aluno cadastrado com sucesso\n")
            print("1- cadastrar outro aluno?")
            print("2- voltar ao menu")

            opcao = int(input("Opção: "))

            if opcao == 2:
                break

    elif menu == 2:
        if len(alunos) == 0:
            print("\n nenhum aluno cadastrado")

        else:
            print("\n ===== LISTA DE ALUNOS =====")
            for aluno in alunos:
                print("Matrícula:", aluno["matricula"])
                print("Nome:", aluno["nome"])
                print("Idade:", aluno["idade"])
                print("Turma:", aluno["turma"])
                print("Notas:")
                print("  Matemática:", aluno["notas"]["matematica"])
                print("  Português:", aluno["notas"]["portugues"])
                print("-----------------------------")

    elif menu == 3:
        while True:

            print("qual aluno deseja procurar?\n")
            Busca_matricula = int(input("Digite a matricula: \n"))

            encontrou = False 
            voltar_menu = False

            for aluno in alunos: 

                if Busca_matricula == aluno["matricula"]:

                    encontrou = True

                    print("-----------------------------")
                    print("Matrícula:", aluno["matricula"])
                    print("Nome:", aluno["nome"])
                    print("Idade:", aluno["idade"])
                    print("Turma:", aluno["turma"])
                    print("Notas:", aluno["matematica"])
                    print("Notas:", aluno["portugues"])
                    print("-----------------------------")

                    print("1- Buscar outro aluno?")
                    print("2- Voltar ao menu")

                    opcao_busca = int(input("Opção"))

                    if opcao_busca == 2:
                        voltar_menu = True
                        break

            if encontrou == False:
                print("aluno não encontrado")

            if voltar_menu == True:
                break

    elif menu == 4:
        while True:
            print("Qual aluno deseja inserir a nota: \n")
            busca_matricula_modificar = int(input("Digite a matrícula: "))

            encontrou = False

            for aluno in alunos:
                if aluno["matricula"] == busca_matricula_modificar:

                    encontrou = True
                    
                    print("Insira as novas notas: ")
                    aluno["matematica"] = float(input("Digite a nova nota de matemática: "))
                    aluno["portugues"] = float(input("Digite a nova nota de português: "))
                    break  

            if not encontrou:
                print("Aluno não encontrado")

            print("1- Buscar outro aluno")
            print("2- Voltar ao menu")
            opcao_busca_modificar = int(input("Opção: "))

            if opcao_busca_modificar == 2:
                break

    elif menu == 5:
        while True:
            print("Qual aluno deseja excluir: \n")
            busca_matricula_excluir = int(input("Digite a matrícula: "))

            encontrou = False

            for aluno in alunos:
                if aluno["matricula"] == busca_matricula_excluir:

                    encontrou = True
                    alunos.remove(aluno)
                    print("Aluno excluído com sucesso!")
                    break  

            if not encontrou:
                print("Aluno não encontrado")

            print("1- Excluir outro aluno")
            print("2- Voltar ao menu")
            opcao_busca_excluir = int(input("Opção: "))

            if opcao_busca_excluir == 2:
                break