import json

dicionario = {
    "CHAVES": ["Chaves do 8", "14/04/2017", "RECEP_001"],
    "QUICO": ["QUICO FLORES", "24/0/2017", "RECP_002"],
    "FLORINDA": ["Florinda Flores", "18/04/2017", "RECP_003"],
}

#with open("bd1.json", "w") as json_file:
    #json.dump(dicionario, json_file)
    
with open("bd.json", "w") as arq_json:
  json.dump(dicionario, arq_json)

with open("bd.json", "r") as arq_json:
    dicionario = json.load(arq_json)
    for chave, dados in dicionario.items():
        print(chave + " | " + str(dados))