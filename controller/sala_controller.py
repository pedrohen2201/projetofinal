"""
Controller responsável por intermediar as ações relacionadas às SALAS
entre a View (interface com o usuário) e o Model (dados das salas).

A view nunca acessa o model diretamente: ela sempre passa pelo
controller, que decide o que fazer com os dados.
"""

from model import sala


def obter_salas():
    """Retorna todas as salas cadastradas."""
    return sala.listar_salas()


def obter_sala(codigo):
    """Retorna uma sala específica pelo código, ou None se não existir."""
    return sala.buscar_sala(codigo)


def adicionar_sala(codigo, nome, capacidade):
    """Solicita ao model o cadastro de uma nova sala."""
    return sala.cadastrar_sala(codigo, nome, capacidade)
