"""
View responsável pela interface textual do sistema.

Toda a interação com o usuário (input e print) acontece aqui.
A view não sabe como os dados são guardados: ela só pede
informações para o controller e mostra o resultado na tela.
"""

from controller import sala_controller
from controller import reserva_controller


def exibir_menu(nome_professor):
    print(f"\n===== SISTEMA DE RESERVA DE SALAS (usuário: {nome_professor}) =====")
    print("1 - Listar salas")
    print("2 - Cadastrar sala")
    print("3 - Reservar sala")
    print("4 - Listar todas as reservas")
    print("5 - Minhas reservas")
    print("6 - Cancelar minha reserva")
    print("0 - Sair")


def tela_listar_salas():
    salas = sala_controller.obter_salas()
    print("\n--- Salas cadastradas ---")
    for s in salas:
        print(f"Código: {s['codigo']} | Nome: {s['nome']} | Capacidade: {s['capacidade']}")


def tela_cadastrar_sala():
    print("\n--- Cadastro de sala ---")
    codigo = input("Código da sala: ")
    nome = input("Nome da sala: ")
    capacidade = int(input("Capacidade da sala: "))

    sucesso = sala_controller.adicionar_sala(codigo, nome, capacidade)
    if sucesso:
        print("Sala cadastrada com sucesso!")
    else:
        print("Já existe uma sala com esse código.")


def tela_reservar_sala(professor):
    print("\n--- Nova reserva ---")
    print("Dias válidos: segunda, terca, quarta, quinta, sexta")
    print("Horários válidos: manha, tarde, noite")

    codigo = input("Código da sala: ")
    dia = input("Dia da semana: ").lower()
    horario = input("Horário (manha/tarde/noite): ").lower()

    resultado = reserva_controller.fazer_reserva(codigo, professor, dia, horario)

    if resultado == "sucesso":
        print("Reserva realizada com sucesso!")
    elif resultado == "sala_inexistente":
        print("Essa sala não existe. Confira o código digitado.")
    elif resultado == "dia_invalido":
        print("Dia informado é inválido.")
    elif resultado == "horario_invalido":
        print("Horário informado é inválido.")
    elif resultado == "conflito":
        print("Já existe uma reserva para essa sala nesse dia e horário.")


def tela_listar_reservas():
    reservas = reserva_controller.obter_reservas()
    print("\n--- Todas as reservas ---")
    if len(reservas) == 0:
        print("Nenhuma reserva cadastrada.")
    for r in reservas:
        print(f"Sala: {r['sala']} | Professor: {r['professor']} | Dia: {r['dia']} | Horário: {r['horario']}")


def tela_minhas_reservas(professor):
    reservas = reserva_controller.obter_reservas_do_professor(professor)
    print(f"\n--- Minhas reservas ({professor}) ---")
    if len(reservas) == 0:
        print("Você ainda não possui reservas.")
    for r in reservas:
        print(f"Sala: {r['sala']} | Dia: {r['dia']} | Horário: {r['horario']}")


def tela_cancelar_reserva(professor):
    print("\n--- Cancelar reserva ---")
    codigo = input("Código da sala: ")
    dia = input("Dia da semana: ").lower()
    horario = input("Horário: ").lower()

    sucesso = reserva_controller.desfazer_reserva(codigo, professor, dia, horario)
    if sucesso:
        print("Reserva cancelada com sucesso!")
    else:
        print("Reserva não encontrada com esses dados.")


def iniciar(usuario_logado):
    """
    Loop principal do programa, já com o professor autenticado.
    usuario_logado é o dicionário retornado pela tela de login.
    """
    nome_professor = usuario_logado["nome"]

    opcao = -1
    while opcao != 0:
        exibir_menu(nome_professor)
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            tela_listar_salas()
        elif opcao == 2:
            tela_cadastrar_sala()
        elif opcao == 3:
            tela_reservar_sala(nome_professor)
        elif opcao == 4:
            tela_listar_reservas()
        elif opcao == 5:
            tela_minhas_reservas(nome_professor)
        elif opcao == 6:
            tela_cancelar_reserva(nome_professor)
        elif opcao == 0:
            print("Encerrando o sistema...")
        else:
            print("Opção inválida.")
