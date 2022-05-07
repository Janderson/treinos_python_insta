def main():
    autor = "Janderson FFerreira @janderson.fferreia"
    print("\n*** Treino - Lista de Tarefas do Dia v1.0 ***"
          f"(por {autor})\n")

    tarefas_do_dia = [
        {"tarefa": "Acordar antes do sol nascer", "feito": True},
        {"tarefa": "Ler 30 minutos de um livro", "feito": True},
        {"tarefa": "Organizar Mentoria Dia #2", "feito": True},
        {"tarefa": "Postar Treino no Instagram", "feito": True},
        {"tarefa": "Pagar Contas (Todas em dia)!", "feito": True},
        {"tarefa": "Assistir um filme com esposa", "feito": False},
    ]

    print(f"\n\n Todas as tarefas: {tarefas_do_dia}")

    tarefas_por_fazer = [tarefa["tarefa"] for tarefa in tarefas_do_dia 
                                if not tarefa["feito"]]

    tarefas_por_fazer_texto = "\n".join(tarefas_por_fazer)
    print(f"\n\nTarefas a fazer:\n{tarefas_por_fazer_texto}")

main()
