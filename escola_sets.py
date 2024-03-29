#!/usr/bin/env python3
"""Exibe um relatorio de estudantes distribuidos por atividades

Imprimi a lista de estudantes agrupadas por sala que frequenta 
cada uma das atividades.
"""

__version__ = "0.1.1"
__author__ = "Pedro Lucas"

sala1 = ["Joao","Luiza","Marta","Ivana","Amanda"]
sala2 = ["Pedro", "Luka","Pina","Laura"]

aula_ingles = ["Joao","Pedro","Ivana","Laura"]
aula_danca = ["Luiza","Pedro","Pina","Amanda"]
aula_musica = ["Luka","Marta","Ivana","Laura"]


atividades = [("Inglês", aula_ingles),
              ("Música", aula_musica),
              ("Dança", aula_danca)]


for nome_atividade, atividade in atividades:

    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)
       
    print(f"Estudantes da aitividade {nome_atividade}:\n")
    print()

    print("Sala1: ",atividade_sala1)
    print("Sala2: ",atividade_sala2)
    print()
    print("#" * 4)

