"""
Módulo responsável por armazenar e manipular os dados das salas de aula.

Aqui ficam apenas os dados (a lista de salas) e as funções que
mexem diretamente nesses dados. Quem chama essas funções é o
controller, nunca a view diretamente.
"""

# Lista de salas cadastradas no sistema.
# Cada sala é representada por um dicionário com código, nome e capacidade.
salas = [
    {"codigo": "A101", "nome": "Sala 101 - Bloco A", "capacidade": 40},
    {"codigo": "A102", "nome": "Sala 102 - Bloco A", "capacidade": 35},
    {"codigo": "B201", "nome": "Sala 201 - Bloco B", "capacidade": 50},
]


def listar_salas():
    """Retorna a lista de todas as salas cadastradas."""
    return salas


def buscar_sala(codigo):
    """Procura uma sala pelo código. Retorna o dicionário da sala ou None."""
    for sala_atual in salas:
        if sala_atual["codigo"] == codigo:
            return sala_atual
    return None


def cadastrar_sala(codigo, nome, capacidade):
    """
    Cadastra uma nova sala na lista, caso o código informado
    ainda não esteja sendo usado por outra sala.
    Retorna True se cadastrou, False se já existia.
    """
    if buscar_sala(codigo) is not None:
        return False

    nova_sala = {"codigo": codigo, "nome": nome, "capacidade": capacidade}
    salas.append(nova_sala)
    return True
