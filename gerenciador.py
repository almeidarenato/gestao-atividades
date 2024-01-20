def adicionar_atividade(lista_de_atividades,nome_atividade):
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

def completar_atividade(lista_de_atividades,indice_atividade):
     indice = int(indice_atividade) -1
     lista_de_atividades[indice]["completada"] = True
     print(f"Atividade {indice_atividade} marcada como completada")
     return

def deletar_atividade(lista_de_atividades,indice_atividade):
     indice = int(indice_atividade)
     for indice_lista,atividade in enumerate(lista_de_atividades,start=1):
          if indice_lista == indice:
             removido = lista_de_atividades.remove(atividade)
             print(f'Atividade {indice}  foi deletada')
             ver_atividades(lista_de_atividades)
             return
          else:
             print(f"Atividade {indice_atividade} não localizada")
     return

def deletar_atividades_completadas(lista_de_atividades):
     for atividade in lista_de_atividades:
          if atividade["completada"] == True:
               lista_de_atividades.remove(atividade)
     print('Atividades completadas foram deletadas')
     ver_atividades(lista_de_atividades)
     return

lista_de_atividades = []

while True: 
    print("\n Menu do Gerenciador de Atividades:")
    print("1. Adicionar atividade")
    print("2. Ver Atividades")
    print("3. Atualizar Atividade")
    print("4. Completar Atividade")
    print("5. Deletar Atividade")
    print("6. Deletar Atividade completadas")
    print("7. Sair")

    escolha = input("Digite a sua opção: ")
    match escolha: 
         case "1":
              nome_atividade = input("Digite o nome da Atividade para adiciona-la:")
              adicionar_atividade(nome_atividade=nome_atividade,lista_de_atividades=lista_de_atividades)
         case "2":
              ver_atividades(lista_de_atividades)
         case "3":
              ver_atividades(lista_de_atividades)
              indice_atividade = input("Digite o número da atividade que deseja atualizar: ")
              novo_nome_atividade = input("Digite o novo nome da atividade: ")
              atualizar_atividade(lista_de_atividades=lista_de_atividades,indice_atividade=indice_atividade,novo_nome_atividade=novo_nome_atividade)
         case "4":
               ver_atividades(lista_de_atividades)
               indice_atividade = input("Digite o número da atividade que deseja completar: ")
               completar_atividade(indice_atividade=indice_atividade,lista_de_atividades=lista_de_atividades)
         case "5":
              ver_atividades(lista_de_atividades)
              indice_atividade = input("Digite o número da atividade que deseja deletar: ")
              deletar_atividade(lista_de_atividades=lista_de_atividades,indice_atividade=indice_atividade)
         case "6":
              deletar_atividades_completadas(lista_de_atividades)
         case "7":
              break

print("Programa finalizado")