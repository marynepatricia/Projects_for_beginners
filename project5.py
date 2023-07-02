compras = list()


while True:
    print("Selecione uma opção: ")
    resp = input("[i]nserir, [a]pagar, [l]istar e [s]air: ").lower()
    if resp not in "ials":
        print("Digite uma opção válida.")
    elif resp == "i":
        item = input("Qual item você quer inserir? ")
        compras.append(item)
    elif resp == "a":
        item_apagar = input("Qual item você deseja apagar? ")
        try:
            indice = int(item_apagar)
            del compras[indice]
        except ValueError:
            print("Por favor, digite um número!")
        except IndexError:
            print("Indice não existe")
        except Exception:
            print("Erro desconhecido.")
    elif resp == "l":
        for i, c in enumerate(compras):
            print(i, c)
    elif len(compras) == 0:
        print("A lista está vazia!")
    elif resp == "s":
        break

print(compras)
