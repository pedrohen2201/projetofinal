"""
Módulo responsável por armazenar e manipular os dados das reservas.

Cada reserva liga uma sala, um professor, um dia da semana e um
horário. Essas listas de dias e horários válidos evitam que o
usuário digite algo fora do padrão esperado.
"""

# Lista de reservas realizadas. Começa vazia.
reservas = []

DIAS_VALIDOS = ["segunda", "terca", "quarta", "quinta", "sexta"]
HORARIOS_VALIDOS = ["manha", "tarde", "noite"]


def listar_reservas():
    """Retorna a lista de todas as reservas cadastradas."""
    return reservas


def existe_conflito(codigo_sala, dia, horario):
    """
    Verifica, percorrendo a lista de reservas, se já existe uma
    reserva para a mesma sala, no mesmo dia e no mesmo horário.
    """
    for reserva_atual in reservas:
        mesma_sala = reserva_atual["sala"] == codigo_sala
        mesmo_dia = reserva_atual["dia"] == dia
        mesmo_horario = reserva_atual["horario"] == horario
        if mesma_sala and mesmo_dia and mesmo_horario:
            return True
    return False


def criar_reserva(codigo_sala, professor, dia, horario):
    """
    Cria uma nova reserva, caso não haja conflito de horário
    para a sala escolhida. Retorna True se conseguiu reservar,
    False caso já exista uma reserva no mesmo horário.
    """
    if existe_conflito(codigo_sala, dia, horario):
        return False

    nova_reserva = {
        "sala": codigo_sala,
        "professor": professor,
        "dia": dia,
        "horario": horario,
    }
    reservas.append(nova_reserva)
    return True


def cancelar_reserva(codigo_sala, professor, dia, horario):
    """
    Procura uma reserva com esses dados exatos e a remove da lista.
    Retorna True se encontrou e cancelou, False se não encontrou.
    """
    for reserva_atual in reservas:
        mesma_sala = reserva_atual["sala"] == codigo_sala
        mesmo_professor = reserva_atual["professor"] == professor
        mesmo_dia = reserva_atual["dia"] == dia
        mesmo_horario = reserva_atual["horario"] == horario
        if mesma_sala and mesmo_professor and mesmo_dia and mesmo_horario:
            reservas.remove(reserva_atual)
            return True
    return False


def reservas_por_professor(professor):
    """Retorna uma lista apenas com as reservas de um professor específico."""
    lista_do_professor = []
    for reserva_atual in reservas:
        if reserva_atual["professor"] == professor:
            lista_do_professor.append(reserva_atual)
    return lista_do_professor
