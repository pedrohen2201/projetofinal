"""
View responsável pela tela de LOGIN e CADASTRO de usuários.

Fica separada do menu.py principal porque representa uma etapa
diferente do sistema: o professor precisa se autenticar antes
de acessar o menu de reservas.
"""

from controller import usuario_controller


def tela_cadastro():
    print("\n--- Cadastro de professor ---")
    login = input("Escolha um login: ")
    senha = input("Escolha uma senha: ")
    nome = input("Nome completo: ")

    sucesso = usuario_controller.registrar(login, senha, nome)
    if sucesso:
        print("Cadastro realizado com sucesso! Agora faça login para continuar.")
    else:
        print("Esse login já está em uso. Tente outro.")


def tela_login():
    print("\n--- Login ---")
    login = input("Login: ")
    senha = input("Senha: ")

    login_valido = usuario_controller.fazer_login(login, senha)
    if login_valido:
        usuario_logado = usuario_controller.obter_usuario(login)
        print(f"Bem-vindo(a), {usuario_logado['nome']}!")
        return usuario_logado
    else:
        print("Login ou senha incorretos.")
        return None


def iniciar_autenticacao():
    """
    Loop de autenticação: fica exibindo o menu de acesso até o
    professor conseguir fazer login (ou escolher sair).
    Retorna o dicionário do usuário logado, ou None se o usuário
    optou por sair.
    """
    usuario_logado = None

    while usuario_logado is None:
        print("\n===== ACESSO AO SISTEMA =====")
        print("1 - Fazer login")
        print("2 - Cadastrar novo professor")
        print("0 - Sair do sistema")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario_logado = tela_login()
        elif opcao == "2":
            tela_cadastro()
        elif opcao == "0":
            return None
        else:
            print("Opção inválida.")

    return usuario_logado
