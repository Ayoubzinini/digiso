from pandas import DataFrame, read_csv
deps=read_csv("/home/az/Downloads/Scrapper/communes-departement-region.csv")
dep_cible=input('dep : ')
dep=deps[deps.code_departement==dep_cible]
communes=dep.nom_commune
communes=communes[2:5]