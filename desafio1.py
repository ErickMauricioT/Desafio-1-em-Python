registros_estudantes = {}


def adicionar_estudante():
    nome = input("Digite o nome do estudante: ")
    ID = input("Digite o ID do estudante: ")
    notas = input("Digite as notas do estudante separadas por espaço: ")
    notas = [int(nota) for nota in notas.split()]
    estudante = {
        "Nome": nome,
        "ID": ID,
        "Notas": notas
    }
    registros_estudantes[ID] = estudante
    print("Registro de estudante adicionado.")


def exibir_registros():
    print("Registros de Estudantes:")
    for ID, estudante in registros_estudantes.items():
        print(f"ID: {ID}")
        print(f"Nome: {estudante['Nome']}")
        print(f"Notas: {estudante['Notas']}")
        print()


def procurar_estudante_por_id():
    ID = input("Digite o ID do estudante que deseja procurar: ")
    estudante = registros_estudantes.get(ID)
    if estudante is not None:
        print("Registro do estudante encontrado:")
        print(f"ID: {ID}")
        print(f"Nome: {estudante['Nome']}")
        print(f"Notas: {estudante['Notas']}")
    else:
        print("Estudante com o ID informado não encontrado.")


def calcular_media_notas():
    total_notas = 0
    total_estudantes = 0

    for estudante in registros_estudantes.values():
        notas = estudante["Notas"]
        total_notas += sum(notas)
        total_estudantes += 1

    if total_estudantes > 0:
        media = total_notas / total_estudantes
        print(f"Média de notas de todos os estudantes: {media:.2f}")
    else:
        print("Não há estudantes registrados para calcular a média.")


def salvar_registros_em_arquivo():
    nome_arquivo = "registros_estudantes.csv"
    
    with open(nome_arquivo, "w") as arquivo:
        for estudante in registros_estudantes.values():
            linha = f"{estudante['Nome']},{estudante['ID']},{','.join(map(str, estudante['Notas']))}\n"
            arquivo.write(linha)

    print(f"Registros de estudantes salvos em {nome_arquivo}")


def carregar_registros_de_arquivo():
    nome_arquivo = "registros_estudantes.csv"
    registros_estudantes.clear()

    try:
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(",")
                nome, ID, notas_str = partes[0], partes[1], partes[2:]
                notas = [int(nota) for nota in notas_str]
                estudante = {
                    "Nome": nome,
                    "ID": ID,
                    "Notas": notas
                }
                registros_estudantes[ID] = estudante

        print(f"Registros de estudantes carregados do arquivo {nome_arquivo}")
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")


adicionar_estudante()
adicionar_estudante()
adicionar_estudante()


exibir_registros()


procurar_estudante_por_id()


calcular_media_notas()


salvar_registros_em_arquivo()


carregar_registros_de_arquivo()