# Código front-end para app buscador das campanhas eleitorais em 2022

def menu_base():
    print("\n\t\t-------- BUSCA ELEIÇÕES 2022 --------")
    print("\n\nOlá! Seja bem-vinda(o) ao buscador das Eleições 2022!")
    print("\n\nO buscador das campanhas eleitorais de 2022 tem como \
objetivo possibilitar ao eleitor a consulta livre de dados referentes \
às campanhas dos candidatos ou coligações dos partidos nas próximas eleições. \
As bases de dados são do Tribunal Superior Eleitoral (TSE) e encontram-se em \
https://dadosabertos.tse.jus.br/dataset/candidatos-2022")
    #Visual do menu
    print("\n\t\t\t########## MENU ##########")
    opc = input("\nDigite a opção desejada: [1]Pesquisar candidato ou [2]Pesquisar partido ou [3]Gerar colinha ou [4]Sair.\n")
    while(opc!="1" and opc!="2" and opc!="3" and opc!="4"):
        print("\nOpção inválida!")
        opc = input("\nDigite a opção desejada: [1]Pesquisar candidato ou [2]Pesquisar partido ou [3]Gerar colinha ou [4]Sair.\n")
    return opc
