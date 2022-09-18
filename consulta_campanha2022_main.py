# Código principal para app buscador das campanhas eleitorais em 2022

from consulta_campanha2022_front import menu_base
from consulta_campanha2022_back import busca_candidatos, busca_coligacoes, gera_colinha

opc = "0"
while opc != "4":
    opc = menu_base()
    if opc == "1":
        busca_candidatos()
    if opc == "2":
        busca_coligacoes()
    if opc == "3":
        gera_colinha()

print("\nAté mais! Faça valer o seu voto!")
