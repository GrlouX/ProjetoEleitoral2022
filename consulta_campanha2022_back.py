# Código back-end para app de busca das campanhas eleitorais em 2022

import unidecode as un
import pandas as pd

#Função que carrega o arquivo de dados dos candidatos nas eleições 2022
def carga_candidatos():
    arq = pd.read_csv("consulta_cand_2022_BRASIL.csv",sep=";",encoding="latin1")
    nome = {}
    cargo = {}
    numero = {}
    partido = {}
    uf_eleicao = {}
    nome_urna = {}
    situacao = {}
    instrucao = {}
    raca = {}
    ocupacao = {}
    reeleicao = {}
    dic_candidatos = (nome, cargo, numero, partido, uf_eleicao, nome_urna, situacao, instrucao, raca, ocupacao, reeleicao)
    for n in range(arq.shape[0]):
        cod = arq.loc[n,"SQ_CANDIDATO"]
        nome.update({cod : arq.loc[n,"NM_CANDIDATO"]})
        cargo.update({cod : arq.loc[n,"DS_CARGO"]})
        numero.update({cod : arq.loc[n,"NR_CANDIDATO"]})
        partido.update({cod : arq.loc[n,"SG_PARTIDO"]})
        uf_eleicao.update({cod : arq.loc[n,"SG_UE"]})
        nome_urna.update({cod : arq.loc[n,"NM_URNA_CANDIDATO"]})
        situacao.update({cod : arq.loc[n,"DS_SITUACAO_CANDIDATO_URNA"]})
        instrucao.update({cod : arq.loc[n,"DS_GRAU_INSTRUCAO"]})
        raca.update({cod : arq.loc[n,"DS_COR_RACA"]})
        ocupacao.update({cod : arq.loc[n,"DS_OCUPACAO"]})
        reeleicao.update({cod : arq.loc[n,"ST_REELEICAO"]})
    return dic_candidatos

#Função que retorna os dados relacionados ao candidato pesquisado
def busca_candidatos():
    pesq = input("\nDigite o nome do candidato a ser pesquisado: ")
    pesq_aux = pesq+"."
    while pesq_aux != pesq:
        for char in ".,;:!?*$%@+=()[]{}<>\/|_0123456789":
            pesq_aux = pesq_aux.replace(char,"")
        if pesq_aux != pesq or pesq_aux == "":
            print("\nO nome do candidato é inválido!")
            pesq = input("\nDigite o nome do candidato a ser pesquisado: ")
            pesq_aux = pesq+"."
    dic_cand = carga_candidatos()
    conj_pesq = set(un.unidecode(pesq).upper().split())
    base_proc = [set(un.unidecode(cand).split()) for cand in dic_cand[0].values()] + \
                [set(un.unidecode(cand).split()) for cand in dic_cand[5].values()]
    if [conj_pesq.issubset(conj) for conj in base_proc].count(True)==0:
        print("\nNenhum dado relacionado ao candidato pesquisado foi encontrado.")
    else:
        list_pesq = [cod for cod in dic_cand[0].keys() if conj_pesq.issubset(set(un.unidecode(dic_cand[0][cod]).split())) and dic_cand[6][cod] == 'DEFERIDO'] + \
                    [cod for cod in dic_cand[0].keys() if conj_pesq.issubset(set(un.unidecode(dic_cand[5][cod]).split())) and dic_cand[6][cod] == 'DEFERIDO']
        if len(list_pesq) == 0:
            print("\nNenhum candidato deferido com o nome pesquisado foi encontrado.")
        else:
            for ind, cod in enumerate(list(set(list_pesq))):
                dados_pesq = "Candidato: " + dic_cand[0][cod] + " (" + dic_cand[5][cod] + ")" + ", cargo: " + dic_cand[1][cod] + \
                             ", nº na urna: " + str(dic_cand[2][cod]) + ", partido: " + dic_cand[3][cod] + \
                             ", instrução: " + dic_cand[7][cod] + ", raça: " + dic_cand[8][cod] + \
                             ", ocupação: " + dic_cand[9][cod] + ", reeleição: " + dic_cand[10][cod]
                print("\nOcorrência",ind+1,"-> ",dados_pesq)
    print("\n\nVerifique se seu candidato já teve as contas julgadas irregulares \
pelo Tribunal de Contas da União em https://contasirregulares.tcu.gov.br/")        
    
#Função que carrega o arquivo de dados das coligações dos partidos nas eleições 2022
def carga_coligacoes():
    arq = pd.read_csv("consulta_coligacao_2022_BRASIL.csv",sep=";",encoding='latin1')
    arq["COD_CHAVE"] = arq["SQ_COLIGACAO"].astype(str) + arq["NR_PARTIDO"].astype(str) + arq["CD_CARGO"].astype(str)
    partido = {}
    sigla = {}
    numero = {}
    tipo = {}
    composicao = {}    
    cargo = {}
    uf_eleicao = {}
    codigo = {}
    situacao = {}
    dic_coligacoes = (partido, sigla, numero, tipo, composicao, cargo, uf_eleicao, codigo, situacao)
    for n in range(arq.shape[0]):
        cod = arq.loc[n,"COD_CHAVE"] # COD_CHAVE = SQ_COLIGACAO + NR_PARTIDO + CD_CARGO*
        partido.update({cod : arq.loc[n,"NM_PARTIDO"]})
        sigla.update({cod : arq.loc[n,"SG_PARTIDO"]})
        numero.update({cod : arq.loc[n,"NR_PARTIDO"]})
        tipo.update({cod : arq.loc[n,"TP_AGREMIACAO"]})
        composicao.update({cod : arq.loc[n,"DS_COMPOSICAO_COLIGACAO"]})
        cargo.update({cod : arq.loc[n,"DS_CARGO"]})
        uf_eleicao.update({cod : arq.loc[n,"SG_UE"]})
        codigo.update({cod : arq.loc[n,"CD_SITUACAO_LEGENDA"]})
        situacao.update({cod : arq.loc[n,"DS_SITUACAO"]})
    return dic_coligacoes

#Função que retorna os dados relacionados ao partido pesquisado
def busca_coligacoes():
    pesq = input("\nDigite o nome do partido a ser pesquisado: ")
    pesq_aux = pesq+"."
    while pesq_aux != pesq:
        for char in ".,;:!?*$%@+=()[]{}<>\/|_0123456789":
            pesq_aux = pesq_aux.replace(char,"")
        if pesq_aux != pesq or pesq_aux == "":
            print("\nO nome do partido é inválido!")
            pesq = input("\nDigite o nome do partido a ser pesquisado: ")
            pesq_aux = pesq+"."
    dic_colig = carga_coligacoes()
    conj_pesq = set(un.unidecode(pesq).upper().split())
    base_proc = [set(un.unidecode(part).split()) for part in dic_colig[0].values()] + \
                [set(un.unidecode(part).split()) for part in dic_colig[1].values()]
    if [conj_pesq.issubset(conj) for conj in base_proc].count(True)==0:
        print("\nNenhum dado relacionado ao partido pesquisado foi encontrado.")
    else:
        list_pesq = [cod for cod in dic_colig[0].keys() if conj_pesq.issubset(set(un.unidecode(dic_colig[0][cod]).split())) and dic_colig[7][cod][0] == 'D'] + \
                    [cod for cod in dic_colig[0].keys() if conj_pesq.issubset(set(un.unidecode(dic_colig[1][cod]).split())) and dic_colig[7][cod][0] == 'D']
        if len(list_pesq) == 0:
            print("\nNenhuma coligação deferida com o nome pesquisado foi encontrada.")
        else:
            for ind, cod in enumerate(list(set(list_pesq))):
                dados_pesq = "Partido: " + dic_colig[0][cod] + " (" + dic_colig[1][cod] + ")" + ", nº da legenda: " + str(dic_colig[2][cod]) + \
                             ", agremiação: " + dic_colig[3][cod] + " " + dic_colig[4][cod] + " para " + dic_colig[5][cod] + " (" + dic_colig[6][cod] + ")" + " - " + dic_colig[8][cod]
                print("\nOcorrência",ind+1,"-> ",dados_pesq)

# Função para gerar arquivo com lista de candidatos para votar
def gera_colinha():
    uf = input("\nDigite a sigla da unidade federativa de sua zona eleitoral: ").upper()
    while uf not in {'MG','SP','RJ','ES','PR','SC','RS','MT','MS','GO','DF','BA','CE','PE','PB','RN','AL','SE','MA','PI','AM','PA','TO','AP','AC','RO','RR'}:
        print("\nSigla da unidade federativa(UF) inválida!")
        uf = input("\nDigite a sigla da UF de sua zona eleitoral com apenas dois caracteres: ").upper()    
    dic_cand = carga_candidatos()
    base_proc = [set(un.unidecode(cand).split()) for cand in dic_cand[0].values()] + \
                [set(un.unidecode(cand).split()) for cand in dic_cand[5].values()]
    list_voto = ["","","","",""]
    confirma = 'N'
    while confirma != 'S' and confirma != 's':
        dep_fed = input("\nDigite o nome do(a) candidato(a) a deputado(a) federal: ")
        conj_dep_fed = set(un.unidecode(dep_fed).upper().split())
        if [conj_dep_fed.issubset(conj) for conj in base_proc].count(True)==0:
            confirma = input("\nSeu voto será computado como inválido. Motivo: Candidato não encontrado. Confirma (tecla ENTER) ou não (qualquer outra tecla)? ")
            list_voto[0] = "BRANCO/NULO"
        else:
            list_dep_fed = [cod for cod in dic_cand[0].keys() if conj_dep_fed.issubset(set(un.unidecode(dic_cand[0][cod]).split())) and dic_cand[1][cod] == 'DEPUTADO FEDERAL' and dic_cand[4][cod] == uf and dic_cand[6][cod] == 'DEFERIDO'] + \
                           [cod for cod in dic_cand[0].keys() if conj_dep_fed.issubset(set(un.unidecode(dic_cand[5][cod]).split())) and dic_cand[1][cod] == 'DEPUTADO FEDERAL' and dic_cand[4][cod] == uf and dic_cand[6][cod] == 'DEFERIDO']
            if len(list(set(list_dep_fed))) > 1:
                for ind, cod in enumerate(list(set(list_dep_fed))):        
                    dados_dep_fed = "Número: " + str(dic_cand[2][cod]) + ", nome completo: " + dic_cand[0][cod] + \
                         ", partido: " + dic_cand[3][cod] + ", reeleição: " + dic_cand[10][cod]
                    print("\nCandidato",ind+1,"-> ",dados_dep_fed)                
                confirma = input("\nSeu voto será computado como inválido. Motivo: Mais de um candidato listado. Confirma (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[0] = "BRANCO/NULO"
            elif len(list_dep_fed) == 0:
                confirma = input("\nSeu voto será computado como inválido. Motivo: Inconsistência entre candidato e cargo. Confirma (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[0] = "BRANCO/NULO"
            else:
                print(f"Número: {str(dic_cand[2][list_dep_fed[0]])}\nNome: {dic_cand[5][list_dep_fed[0]]}\nPartido: {dic_cand[3][list_dep_fed[0]]}\n")
                confirma = input("Confirma este voto (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[0] = f"{dic_cand[5][list_dep_fed[0]]} - {str(dic_cand[2][list_dep_fed[0]])}"    
    confirma = 'N'
    while confirma != 'S' and confirma != 's':
        dep_reg = input("\nDigite o nome do(a) candidato(a) a deputado(a) estadual ou distrital: ")
        conj_dep_reg = set(un.unidecode(dep_reg).upper().split())
        if [conj_dep_reg.issubset(conj) for conj in base_proc].count(True)==0:
            confirma = input("\nSeu voto será computado como inválido. Motivo: Candidato não encontrado. Confirma (tecla S) ou não (qualquer outra tecla)? ")
            list_voto[1] = "BRANCO/NULO"
        else:
            list_dep_reg = [cod for cod in dic_cand[0].keys() if conj_dep_reg.issubset(set(un.unidecode(dic_cand[0][cod]).split())) and dic_cand[1][cod] in {'DEPUTADO ESTADUAL','DEPUTADO DISTRITAL'} and dic_cand[4][cod] == uf and dic_cand[6][cod] == 'DEFERIDO'] + \
                           [cod for cod in dic_cand[0].keys() if conj_dep_reg.issubset(set(un.unidecode(dic_cand[5][cod]).split())) and dic_cand[1][cod] in {'DEPUTADO ESTADUAL','DEPUTADO DISTRITAL'} and dic_cand[4][cod] == uf and dic_cand[6][cod] == 'DEFERIDO']
            if len(list(set(list_dep_reg))) > 1:
                for ind, cod in enumerate(list(set(list_dep_reg))):
                    dados_dep_reg = "Número: " + str(dic_cand[2][cod]) + ", nome completo: " + dic_cand[0][cod] + \
                         ", partido: " + dic_cand[3][cod] + ", reeleição: " + dic_cand[10][cod]
                    print("\nCandidato",ind+1,"-> ",dados_dep_reg)                
                confirma = input("\nSeu voto será computado como inválido. Motivo: Mais de um candidato listado. Confirma (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[1] = "BRANCO/NULO"
            elif len(list_dep_reg) == 0:
                confirma = input("\nSeu voto será computado como inválido. Motivo: Inconsistência entre candidato e cargo. Confirma (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[1] = "BRANCO/NULO"
            else:
                print(f"Número: {str(dic_cand[2][list_dep_reg[0]])}\nNome: {dic_cand[5][list_dep_reg[0]]}\nPartido: {dic_cand[3][list_dep_reg[0]]}\n")
                confirma = input("Confirma este voto (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[1] = f"{dic_cand[5][list_dep_reg[0]]} - {str(dic_cand[2][list_dep_reg[0]])}"    
    confirma = 'N'
    while confirma != 'S' and confirma != 's':
        sen_rep = input("\nDigite o nome do(a) candidato(a) a senador(a): ")
        conj_sen_rep = set(un.unidecode(sen_rep).upper().split())
        if [conj_sen_rep.issubset(conj) for conj in base_proc].count(True)==0:
            confirma = input("\nSeu voto será computado como inválido. Motivo: Candidato não encontrado. Confirma (tecla S)? ")
            list_voto[2] = "BRANCO/NULO"
        else:
            list_sen_rep = [cod for cod in dic_cand[0].keys() if conj_sen_rep.issubset(set(un.unidecode(dic_cand[0][cod]).split())) and dic_cand[1][cod] == 'SENADOR' and dic_cand[4][cod] == uf and dic_cand[6][cod] == 'DEFERIDO'] + \
                           [cod for cod in dic_cand[0].keys() if conj_sen_rep.issubset(set(un.unidecode(dic_cand[5][cod]).split())) and dic_cand[1][cod] == 'SENADOR' and dic_cand[4][cod] == uf and dic_cand[6][cod] == 'DEFERIDO']
            if len(list(set(list_sen_rep))) > 1:
                for ind, cod in enumerate(list(set(list_sen_rep))):
                    dados_sen_rep = "Número: " + str(dic_cand[2][cod]) + ", nome completo: " + dic_cand[0][cod] + \
                         ", partido: " + dic_cand[3][cod] + ", reeleição: " + dic_cand[10][cod]
                    print("\nCandidato",ind+1,"-> ",dados_sen_rep)                
                confirma = input("\nSeu voto será computado como inválido. Motivo: Mais de um candidato listado. Confirma (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[2] = "BRANCO/NULO"
            elif len(list_sen_rep) == 0:
                confirma = input("\nSeu voto será computado como inválido. Motivo: Inconsistência entre candidato e cargo. Confirma (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[2] = "BRANCO/NULO"
            else:
                list_sen_rep_sup = [cod for cod in dic_cand[0].keys() if dic_cand[0][cod] != dic_cand[0][list_sen_rep[0]] and dic_cand[2][cod] == dic_cand[2][list_sen_rep[0]] and dic_cand[4][cod] == uf and dic_cand[1][cod] == '1º SUPLENTE'] + \
                                   [cod for cod in dic_cand[0].keys() if dic_cand[0][cod] != dic_cand[0][list_sen_rep[0]] and dic_cand[2][cod] == dic_cand[2][list_sen_rep[0]] and dic_cand[4][cod] == uf and dic_cand[1][cod] == '2º SUPLENTE']
                print(f"Número: {str(dic_cand[2][list_sen_rep[0]])}\nNome: {dic_cand[5][list_sen_rep[0]]}\nPartido: {dic_cand[3][list_sen_rep[0]]}\n1º Suplente: {dic_cand[5][list_sen_rep_sup[0]]}\n2º Suplente: {dic_cand[5][list_sen_rep_sup[1]]}\n")
                confirma = input("Confirma este voto (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[2] = f"{dic_cand[5][list_sen_rep[0]]} - {str(dic_cand[2][list_sen_rep[0]])}"    
    confirma = 'N'
    while confirma != 'S' and confirma != 's':
        gov_est = input("\nDigite o nome do(a) candidato(a) a governador(a): ")
        conj_gov_est = set(un.unidecode(gov_est).upper().split())
        if [conj_gov_est.issubset(conj) for conj in base_proc].count(True)==0:
            confirma = input("\nSeu voto será computado como inválido. Motivo: Candidato não encontrado. Confirma (tecla S) ou não (qualquer outra tecla)? ")
            list_voto[3] = "BRANCO/NULO"
        else:
            list_gov_est = [cod for cod in dic_cand[0].keys() if conj_gov_est.issubset(set(un.unidecode(dic_cand[0][cod]).split())) and dic_cand[1][cod] == 'GOVERNADOR' and dic_cand[4][cod] == uf and dic_cand[6][cod] == 'DEFERIDO'] + \
                           [cod for cod in dic_cand[0].keys() if conj_gov_est.issubset(set(un.unidecode(dic_cand[5][cod]).split())) and dic_cand[1][cod] == 'GOVERNADOR' and dic_cand[4][cod] == uf and dic_cand[6][cod] == 'DEFERIDO']
            if len(list(set(list_gov_est))) > 1:
                for ind, cod in enumerate(list(set(list_gov_est))):
                    dados_gov_est = "Número: " + str(dic_cand[2][cod]) + ", nome completo: " + dic_cand[0][cod] + \
                         ", partido: " + dic_cand[3][cod] + ", reeleição: " + dic_cand[10][cod]
                    print("\nCandidato",ind+1,"-> ",dados_gov_est)                
                confirma = input("\nSeu voto será computado como inválido. Motivo: Mais de um candidato listado. Confirma (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[3] = "BRANCO/NULO"
            elif len(list_gov_est) == 0:
                confirma = input("\nSeu voto será computado como inválido. Motivo: Inconsistência entre candidato e cargo. Confirma (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[3] = "BRANCO/NULO"
            else:
                list_gov_est_vice = [cod for cod in dic_cand[0].keys() if dic_cand[0][cod] != dic_cand[0][list_gov_est[0]] and dic_cand[2][cod] == dic_cand[2][list_gov_est[0]] and dic_cand[4][cod] == uf and dic_cand[1][cod] == 'VICE-GOVERNADOR']
                print(f"Número: {str(dic_cand[2][list_gov_est[0]])}\nNome: {dic_cand[5][list_gov_est[0]]}\nPartido: {dic_cand[3][list_gov_est[0]]}\nVice: {dic_cand[5][list_gov_est_vice[0]]}\n")
                confirma = input("Confirma este voto (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[3] = f"{dic_cand[5][list_gov_est[0]]} - {str(dic_cand[2][list_gov_est[0]])}"    
    confirma = 'N'
    while confirma != 'S' and confirma != 's':
        pres_rep = input("\nDigite o nome do(a) candidato(a) a presidente: ")
        conj_pres_rep = set(un.unidecode(pres_rep).upper().split())
        if [conj_pres_rep.issubset(conj) for conj in base_proc].count(True)==0:
            confirma = input("\nSeu voto será computado como inválido. Motivo: Candidato não encontrado. Confirma (tecla S) ou não (qualquer outra tecla)? ")
            list_voto[4] = "BRANCO/NULO"
        else:
            list_pres_rep = [cod for cod in dic_cand[0].keys() if conj_pres_rep.issubset(set(un.unidecode(dic_cand[0][cod]).split())) and dic_cand[1][cod] == 'PRESIDENTE' and dic_cand[4][cod] == 'BR' and dic_cand[6][cod] == 'DEFERIDO'] + \
                            [cod for cod in dic_cand[0].keys() if conj_pres_rep.issubset(set(un.unidecode(dic_cand[5][cod]).split())) and dic_cand[1][cod] == 'PRESIDENTE' and dic_cand[4][cod] == 'BR' and dic_cand[6][cod] == 'DEFERIDO']
            if len(list(set(list_pres_rep))) > 1:
                for ind, cod in enumerate(list(set(list_pres_rep))):
                    dados_pres_rep = "Número: " + str(dic_cand[2][cod]) + ", nome completo: " + dic_cand[0][cod] + \
                         ", partido: " + dic_cand[3][cod] + ", reeleição: " + dic_cand[10][cod]
                    print("\nCandidato",ind+1,"-> ",dados_pres_rep)                
                confirma = input("\nSeu voto será computado como inválido. Motivo: Mais de um candidato listado. Confirma (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[4] = "BRANCO/NULO"
            elif len(list_pres_rep) == 0:
                confirma = input("\nSeu voto será computado como inválido. Motivo: Inconsistência entre candidato e cargo. Confirma (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[4] = "BRANCO/NULO"
            else:
                list_pres_rep_vice = [cod for cod in dic_cand[0].keys() if dic_cand[0][cod] != dic_cand[0][list_pres_rep[0]] and dic_cand[2][cod] == dic_cand[2][list_pres_rep[0]] and dic_cand[4][cod] == 'BR' and dic_cand[1][cod] == 'VICE-PRESIDENTE']
                print(f"Número: {str(dic_cand[2][list_pres_rep[0]])}\nNome: {dic_cand[5][list_pres_rep[0]]}\nPartido: {dic_cand[3][list_pres_rep[0]]}\nVice: {dic_cand[5][list_pres_rep_vice[0]]}\n")
                confirma = input("Confirma este voto (tecla S) ou não (qualquer outra tecla)? ")
                list_voto[4] = f"{dic_cand[5][list_pres_rep[0]]} - {str(dic_cand[2][list_pres_rep[0]])}"
    print("\t\t\n**************************FIM*****************************")            
    arq = open("cola_eleitoral.txt",mode="w")
    arq.write(f"\t\t________COLINHA ELEITORAL 2022_________\n\n")
    arq.write(f"\nDeputado(a) Federal: {list_voto[0]}\n")
    arq.write(f"\nDeputado(a) Estadual: {list_voto[1]}\n")
    arq.write(f"\nSenador(a): {list_voto[2]}\n")
    arq.write(f"\nGovernador(a): {list_voto[3]}\n")
    arq.write(f"\nPresidente: {list_voto[4]}\n")
    arq.close()
