def adicionar_atividade(lista_de_atividades,nome_atividade):
    # atividade = nome da atividade
    # completada = indica de a atividade foi finalizada
    atividade = {"atividade":nome_atividade,"completada": False}
    lista_de_atividades.append(atividade)
    print(f"Atividade {nome_atividade} adicionada com sucesso")
    return

def ver_atividades(lista_de_atividades):
    print("\n Lista de Tarefas")
    for indice,atividade in enumerate(lista_de_atividades, start=1):
        status = "✓" if atividade["completada"] else " "
        nome_atividade = atividade["atividade"]
        print(f"{indice}- [{status}] {nome_atividade}")
        return

def atualizar_atividade(lista_de_atividades,indice_atividade,novo_nome_atividade):
    indice = int(indice_atividade) -1
    print(len(lista_de_atividades))
    if indice >= 0 and indice< len(lista_de_atividades) :
            lista_de_atividades[indice]["atividade"] = novo_nome_atividade
            print(f"Tarefa {indice_atividade} atualizada para {novo_nome_atividade}")
    else:
            print("Numero de tarefa inexistente")
    return


lista_de_atividades = []

while True: 
    print("\n Menu do Gerenciador de Atividades:")
    print("1. Adicionar atividade")
    print("2. Ver Atividades")
    print("3. Atualizar Atividade")
    print("4. Completar Atividade")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua opção: ")
    if escolha == "1":
        nome_atividade = input("Digite o nome da Atividade para adiciona-la:")
        adicionar_atividade(nome_atividade=nome_atividade,lista_de_atividades=lista_de_atividades)
    elif escolha == "2":
        ver_atividades(lista_de_atividades)
    elif escolha =="3":
        ver_atividades(lista_de_atividades)
        indice_atividade = input("Digite o número da atividade: ")
        novo_nome_atividade = input("Digite o novo nome da atividade: ")
        atualizar_atividade(lista_de_atividades=lista_de_atividades,indice_atividade=indice_atividade,novo_nome_atividade=novo_nome_atividade)
    elif escolha =="6":
        break
    


print("Programa finalizado")