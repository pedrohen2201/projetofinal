"""
Controller responsável por intermediar as ações relacionadas às RESERVAS
entre a View (interface com o usuário) e o Model (dados das reservas).

Aqui também ficam as regras de negócio, como validar se a sala existe
e se o dia/horário informados são válidos antes de mandar o model
criar a reserva.
"""

from model import sala
from model import reserva


def fazer_reserva(codigo_sala, professor, dia, horario):
    """
    Valida os dados da reserva e, se tudo estiver correto, pede ao
    model para criá-la. Retorna uma string indicando o resultado:
    "sucesso", "sala_inexistente", "dia_invalido",
    "horario_invalido" ou "conflito".
    """
    sala_encontrada = sala.buscar_sala(codigo_sala)
    if sala_encontrada is None:
        return "sala_inexistente"

    if dia not in reserva.DIAS_VALIDOS:
        return "dia_invalido"

    if horario not in reserva.HORARIOS_VALIDOS:
        return "horario_invalido"

    conseguiu_reservar = reserva.criar_reserva(codigo_sala, professor, dia, horario)
    if conseguiu_reservar:
        return "sucesso"
    else:
        return "conflito"


def obter_reservas():
    """Retorna todas as reservas cadastradas."""
    return reserva.listar_reservas()


def obter_reservas_do_professor(professor):
    """Retorna as reservas de um professor específico."""
    return reserva.reservas_por_professor(professor)


def desfazer_reserva(codigo_sala, professor, dia, horario):
    """Solicita ao model o cancelamento de uma reserva."""
    return reserva.cancelar_reserva(codigo_sala, professor, dia, horario)
