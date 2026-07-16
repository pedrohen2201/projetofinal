"""
Controller responsável por intermediar as ações de LOGIN e CADASTRO
de usuários (professores) entre a View e o Model.
"""

from model import usuario


def registrar(login, senha, nome):
    """Solicita ao model o cadastro de um novo usuário."""
    return usuario.cadastrar_usuario(login, senha, nome)


def fazer_login(login, senha):
    """Verifica se login e senha são válidos."""
    return usuario.validar_login(login, senha)


def obter_usuario(login):
    """Retorna os dados de um usuário a partir do login."""
    return usuario.buscar_usuario(login)
