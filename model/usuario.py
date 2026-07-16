"""
Módulo responsável por armazenar e manipular os dados dos usuários
(professores) que podem acessar o sistema.
"""

# Lista de usuários cadastrados. Já vem com um usuário padrão.
usuarios = [
    {"login": "admin", "senha": "admin123", "nome": "Administrador"},
]


def buscar_usuario(login):
    """Procura um usuário pelo login. Retorna o dicionário ou None."""
    for usuario_atual in usuarios:
        if usuario_atual["login"] == login:
            return usuario_atual
    return None


def cadastrar_usuario(login, senha, nome):
    """
    Cadastra um novo usuário, caso o login informado ainda não
    esteja sendo usado. Retorna True se cadastrou, False se já existia.
    """
    if buscar_usuario(login) is not None:
        return False

    novo_usuario = {"login": login, "senha": senha, "nome": nome}
    usuarios.append(novo_usuario)
    return True


def validar_login(login, senha):
    """
    Verifica se existe um usuário com esse login e se a senha
    informada confere. Retorna True ou False.
    """
    usuario_encontrado = buscar_usuario(login)
    if usuario_encontrado is None:
        return False
    return usuario_encontrado["senha"] == senha
