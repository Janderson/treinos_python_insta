def main():
    autor = "Janderson FFerreira @janderson.fferreia"
    print(f"\n*** Treino - Lista de Tarefas do Dia v1.0 *** (por {autor})\n")

    tarefas_do_dia = [
        {"tarefa": "Acordar antes do sol nascer", "feito": True},
        {"tarefa": "Ler 30 minutos de um livro", "feito": True},
        {"tarefa": "Organizar Mentoria Dia #2", "feito": True},
        {"tarefa": "Postar Treino no Instagram", "feito": True},
        {"tarefa": "Pagar Contas (Todas em dia)!", "feito": True},
        {"tarefa": "Assistir um filme", "feito": False},
    ]

    print(f"Todas as tarefas: {tarefas_do_dia}")

    tarefas_por_fazer = [tarefa for tarefa in tarefas_do_dia if tarefa["feito"]]

    print(f"Tarefas a fazer: {tarefas_por_fazer}")

main()
