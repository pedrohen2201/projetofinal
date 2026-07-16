"""
Ponto de entrada do Sistema de Reserva de Salas de Aula.

Este arquivo apenas orquestra o fluxo geral do programa:
1. Mostra a tela de autenticação (login/cadastro).
2. Se o professor conseguir se autenticar, abre o menu principal.
3. Se o professor optar por sair na tela de autenticação, encerra o sistema.

Toda a lógica de interface fica nas views (view/login_view.py e
view/menu.py), e todo o acesso aos dados passa pelos controllers.
Este arquivo não conhece detalhes de model nem de controller.
"""

from view import login_view
from view import menu


def main():
    print("Bem-vindo ao Sistema de Reserva de Salas de Aula!")

    usuario_logado = login_view.iniciar_autenticacao()

    if usuario_logado is None:
        print("Até logo!")
        return

    menu.iniciar(usuario_logado)


if __name__ == "__main__":
    main()
