def adicionar_atividade(lista_de_atividades,nome_atividade):
    # atividade = nome da atividade
    # completada = indica de a atividade foi finalizada
    atividade = {"atividade":nome_atividade,"completada": False}
    lista_de_atividades.append(atividade)
    print(f"Atividade {nome_atividade} adicionada com sucesso")
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
    if escolha =="6":
        break
    


print("Programa finalizado")