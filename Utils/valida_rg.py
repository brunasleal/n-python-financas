import re


def valida_rg():

    padrao_rg = r'(^\d{1,2}).?(\d{3}).?(\d{3})-?(\d{1}|X|x$)'

    while True:
        rg = input("RG: ")
        if re.match(padrao_rg, rg):
            return rg
        else:
            print("RG inválido. Tente novamente.")


if __name__ == "__main__":
    print(valida_rg())
