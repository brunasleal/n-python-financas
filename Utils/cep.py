import re

import requests


def busca_cep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            endereco = {
                "CEP": data['cep'],
                "Logradouro": data['logradouro'],
                "Complemento": data['complemento'],
                "Bairro": data['bairro'],
                "Cidade": data['localidade'],
                "Estado": data['uf']
            }

            return endereco


def valida_cep():
    padrao_cep = r'(^[0-9]{5})-?([0-9]{3}$)'

    print("Consulta do CEP - ViaCEP")

    while True:
        cep_input = input("CEP: ")
        retorno_cep = busca_cep(cep_input)

        if re.match(padrao_cep, cep_input):
            return retorno_cep
        else:
            print("CPF inválido, digite novamente: ")


if __name__ == "__main__":
    print(valida_cep())
