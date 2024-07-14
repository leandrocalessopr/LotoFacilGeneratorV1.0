"""
   Se foi últil para você de alguma forma, então faça um doação em Crypto.
   
     * Ethereum   : 0xd29b2ff62842f4fd9864caf410155be0ebc2a132
     * Bitcoin    : 15jzC1ynahB187RRxEthgE1Pv1xXZ7EYbW   
     * Zec(Zcash) : tex123as8jgwljy5c3pyx495lyqwm34prywa68tfv2
     * Dash       : XgajTRdHg97VaTwJFrNvqRP8Va1vz6ypd8

"""

import itertools
import random
import re

import requests

LISTA_TODOS_JOGOS          = []
LISTA_TODAS_POSSIBILIDADES = [] # Menos os jogos que já saíram.
NOME_ARQUIVO               = "totalPossibilidades.txt"
CONTADOR                   = 0  # contador, sequências geradas.

def extrai_todos_jogos_site():

    global LISTA_TODOS_JOGOS

    url = "https://asloterias.com.br/lista-de-resultados-da-lotofacil"
    response = requests.get(url, verify=False)
    html = response.text
    padrao = r'\d+(?: \d+){14}'
    pattern = re.compile(padrao)
    lista_match = pattern.findall(html)
    for string in lista_match:
        lista_substrings = string.split()
        LISTA_TODOS_JOGOS.append([int(substring) for substring in lista_substrings])

def generate_loto_facil_sequence():

    return sorted ( random.sample(range(1, 26), 15) )

def generate_combinations():

    # Cria uma lista de 25 números (1 a 25)
    #numbers = list(range(1, 26))

    # Gera todas as combinações de 15 números escolhidos entre 25
    #combinations = itertools.combinations(numbers, 15)

    global CONTADOR

    aux  = False
    while ( not aux ) :
         combination = generate_loto_facil_sequence()
         if not compara_jogos_sorteados( combination ) :
            if analize_unidades ( combination ) :
               if sinteze_subsequencias( combination ) :
                  if not analize_espelho( combination ) :
                     if analize_numeros_anterior( combination ) :
                        if analise_atrasadas( combination) :
                           if analise_evidencia( combination ) :
                              CONTADOR += 1
                              print( str ( CONTADOR ) + " - " + format_sequencia( sorted ( combination ) ) )
                              aux = True

""" Recebe uma lista de 15 numeros e compara com todos os jogos ja sorteados. 
    Se ouver Match retorna true.
"""
def compara_jogos_sorteados( lista_param ):

    global LISTA_TODOS_JOGOS

    for lista_sorteada in LISTA_TODOS_JOGOS :
        if lista_sorteada == lista_param :
            return True
    return False

def guarda_em_arquivo() :

    # Abrir o arquivo no modo de escrita ('w' cria o arquivo se ele não existir)
    arquivo = open ( NOME_ARQUIVO, 'w' )
    cont = 1
    str_sequencia = ""
    for sequencia in LISTA_TODAS_POSSIBILIDADES :
        str_sequencia = format_sequencia( sequencia )
        print( str ( cont ) + ") " + str_sequencia )
        arquivo.write( str( cont ) + ")" + str_sequencia + "\n")
        cont += 1
    arquivo.close()

def format_sequencia( lista_param ):

    str_result = ""

    for dezena in lista_param :
        if dezena < 10 : str_result += "0" + str ( dezena ) + " "
        else : str_result += str ( dezena ) + " "

    return  str_result.rstrip()

def analize_unidades ( lista ):

    menores = list(filter(lambda x: x < 10, lista))

    if len(menores) >= 4 and len(menores) <= 7 : return True

    return False

def analize_espelho( possibilidade_param ) :

    lista_conj_testar = [ [ v + 1 for v in possibilidade_param ], [ v - 1 for v in possibilidade_param ] ]
    cont = 0
    while cont < len ( lista_conj_testar ) :
        if compara_jogos_sorteados( lista_conj_testar [ cont ] ) :
           return True
        cont += 1

    return False

"""
   Verifica se as sequencias de quatorze do jogo gerado jà se repetiu em algum jogo sorteado.
"""
def analize_sequencias_quatorze(possibilidade_param):

    global LISTA_TODOS_JOGOS

    for sequencia_sorteada in LISTA_TODOS_JOGOS:
        for j in range (0, 2 ):  # Para as sub-sequências dentro do possibilidade_param
            possibilidade_quatorze_j = sequencia_sorteada [ j : j + 14]
            for i in range (0, 2 ):
                possibilidade_quatorze_i = possibilidade_param [ i : i + 14]
                if possibilidade_quatorze_j == possibilidade_quatorze_i :
                   return True
    return False

"""  
   Verifica se as sequencias de treze do jogo gerado jà se repetiu em algum jogo sorteado.
"""
def analize_sequencias_treze(possibilidade_param):

    global LISTA_TODOS_JOGOS

    for sequencia_sorteada in LISTA_TODOS_JOGOS:
        for j in range (0, 3 ):  # Para as sub-sequências dentro do possibilidade_param
            possibilidade_treze_j = sequencia_sorteada [ j : j + 13]
            for i in range (0, 3 ):
                possibilidade_treze_i = possibilidade_param [ i : i + 13]
                if possibilidade_treze_j == possibilidade_treze_i :
                   return True
    return False

def analize_sequencias_doze(possibilidade_param):

    global LISTA_TODOS_JOGOS

    for sequencia_sorteada in LISTA_TODOS_JOGOS:
        for j in range (0, 4 ):  # Para as sub-sequências dentro do possibilidade_param
            possibilidade_doze_j = sequencia_sorteada [ j : j + 12]
            for i in range (0, 4 ):
                possibilidade_doze_i = possibilidade_param [ i : i + 12]
                if possibilidade_doze_j == possibilidade_doze_i :
                   return True
    return False

def analize_sequencias_onze(possibilidade_param):

    global LISTA_TODOS_JOGOS

    for sequencia_sorteada in LISTA_TODOS_JOGOS:
        for j in range (0, 5 ):  # Para as sub-sequências dentro do possibilidade_param
            possibilidade_onze_j = sequencia_sorteada [ j : j + 11]
            for i in range (0, 5 ):
                possibilidade_onze_i = possibilidade_param [ i : i + 11]
                if possibilidade_onze_j == possibilidade_onze_i :
                   return True
    return False

def analize_sequencias_dez(possibilidade_param):

    global LISTA_TODOS_JOGOS

    for sequencia_sorteada in LISTA_TODOS_JOGOS:
        for j in range (0, 6 ):  # Para as sub-sequências dentro do possibilidade_param
            possibilidade_dez_j = sequencia_sorteada [ j : j + 10]
            for i in range (0, 6 ):
                possibilidade_dez_i = possibilidade_param [ i : i + 10]
                if possibilidade_dez_j == possibilidade_dez_i :
                   return True
    return False

def sinteze_subsequencias( possibilidade_param ) :

    if analize_sequencias_dez( possibilidade_param ) or analize_sequencias_onze( possibilidade_param ) :
       if not analize_sequencias_doze( possibilidade_param ) :
          if not analize_sequencias_treze( possibilidade_param ) :
             if not analize_sequencias_quatorze( possibilidade_param ) :
                return True

    return False

def analize_numeros_anterior( possibilidade_para ) :

    unidades = []
    dezenas  = []
    convergem   = list ( set ( LISTA_TODOS_JOGOS [ 0 ] ) & set ( possibilidade_para ) )

    if len ( convergem ) >= 8 and len ( convergem ) <= 10 :
      unidades = [ v for v in convergem if v < 10 ]
      dezenas  = [ v for v in convergem if v >= 10 ]

    if len ( dezenas ) > len ( unidades ) : return True

    """"
    if ( int( len(unidades) / len(convergem) * 100 ) >= 30 and int( len(unidades) / len(convergem) * 100 ) <= 35) :
       return True
    """

    return False

def analise_atrasadas( possibilidade_para ) :

    global LISTA_TODOS_JOGOS

    dicio_numeros = { key : 0 for key in range ( 1, 26 ) }

    for key in dicio_numeros.keys() :
       contador = 0

       for sequencia in LISTA_TODOS_JOGOS :
           if not key in sequencia :
              contador += 1
           else : break

       if contador > 0 :
          dicio_numeros [ key ] = contador

    dicio_aux = list ( { v for v in dicio_numeros.values() if v > 3} )
    res       = all ( elemento in possibilidade_para for elemento in dicio_aux )

    if res : return True

    return False

def analise_evidencia( possibilidade_para ):

    global LISTA_TODOS_JOGOS

    dicio_numeros = { key : 0 for key in range ( 1, 26 ) }

    for key in dicio_numeros.keys() :
       contador = 0

       for sequencia in LISTA_TODOS_JOGOS :
           if key in sequencia :
              contador += 1
           else : break

       if contador > 0 :
          dicio_numeros [ key ] = contador

    dicio_aux = list ( { v for v in dicio_numeros.values() if v > 3} )
    res       = all ( elemento not in possibilidade_para for elemento in dicio_aux )

    if res == True : return True

    return False

if __name__ == '__main__':

   extrai_todos_jogos_site()
   print("extrai_todos_jogos_site ____OK")

   total_sequencias = int ( input("Quantas sequências ? ") )
   cont = 0
   while(cont < total_sequencias) :
        generate_combinations()
        cont += 1


   #guarda_em_arquivo()
   #print("guarda_em_arquivo____OK")
