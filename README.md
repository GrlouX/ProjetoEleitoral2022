# Projeto Eleitoral 2022

**Objetivo**: Criação de uma interface para pesquisar candidatos e partidos das Eleições 2022 no Brasil, que possibilite ao usuário/eleitor uma interação facilitada com dados
reais extraídos da base do Tribunal Superior Eleitoral (TSE).

## Funcionalidades

O código pode ser baixado neste repositório como arquivo compactado (zip) para ser executado na máquina local. Esse arquivo zip contém as bases de dados mais recentes
disponibilizadas no site do TSE para candidatos e coligações, além dos dicionários de dados que explicam cada uma das variáveis presentes.

A aplicação desenvolvida possui três funcionalidades básicas:

1) **"Pesquisar candidatos"**: O usuário poderá digitar o nome do candidato desejado (mesmo incompleto ou tal como ele é conhecido) e o sistema retornará diversos dados
referentes ao candidato pesquisado, a saber - nome completo do candidato, nome do candidato que aparecerá na urna (entre parênteses), cargo disputado pelo candidato,
número na urna, partido que integra, grau de instrução, cor/raça autodeclarada, ocupação informada e se concorre à reeleição (S- Sim, N- Não). Somente os candidatos com
situação da candidatura para o pleito deferida pela Justiça Eleitoral aparecerão na pesquisa.

2) **"Pesquisar partidos"**: O usuário poderá digitar o nome ou a sigla do partido desejado e o sistema retornará os seguintes dados relativos ao partido pesquisado - nome
completo do partido, sigla do partido (entre parênteses), número da legenda do partido, tipo de agremiação do qual faz parte (partido isolado, federação ou coligação), 
sigla(s) do(s) partido(s) que integra(m) a agremiação, cargo em disputa e unidade federativa (UF) referentes à agremiação do partido. Somente as agremiações com situação
deferida pela Justiça Eleitoral aparecerão na pesquisa.

3) **"Gerar colinha"**: Simulador da votação no dia do primeiro turno das Eleições 2022, com todos os candidatos reais (com situação deferida) e cargos em disputa na
ordem em que aparecerão na urna, separados por unidade federativa (UF). Para isso, o usuário *deverá digitar a sigla de sua UF (com dois caracteres)* e poderá gerar a
lista dos candidatos com seus respectivos números para levar no dia da eleição, caso queira. O sistema perguntará o nome do candidato nos mesmos moldes do item 1. *Caso o 
usuário não saiba quem são os candidatos ao cargo em questão na sua UF, poderá ter acesso a todos eles ao apertar a tecla ENTER.* Em seguida, terá a opção de confirmar o 
voto (tecla S) ou não (qualquer outra tecla). *Deve-se ficar atento(a) à mensagem de confirmação que aparecerá na tela, pois ela indicará eventuais erros que o usuário
poderá corrigir antes de confirmar o voto para cada cargo.* Após finalizar a simulação, será gerado o arquivo de texto "cola_eleitoral.txt", o qual poderá ser baixado
pelo usuário.

## Versão web

- Link de acesso: [bit.ly/3DPMCZM](https://colab.research.google.com/drive/1IX0ff54QBk7KxcmrUliChf7s7P5PhQLR)
- QR Code:
  
![bit ly_3DPMCZM](https://user-images.githubusercontent.com/90117229/192120316-8f157fee-5f5a-4589-a528-891303f8ef31.png)

### Links úteis

- Fonte de dados: [Dados Abertos do Tribunal Superior Eleitoral (TSE)](https://dadosabertos.tse.jus.br/dataset/candidatos-2022)
- Dados de contas eleitorais: [Contas Eleitorais pelo Tribunal de Contas da União (TCU)](https://contasirregulares.tcu.gov.br)

