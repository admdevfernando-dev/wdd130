# Projeto: Recibo da Mercearia (CSE 111)

import csv
from datetime import datetime


def ler_dicionario(nome_arquivo, indice_coluna_chave):
    
    dicionario = {}
    arquivo_csv = open(nome_arquivo, "r", encoding="utf-8")
    leitor_csv = csv.reader(arquivo_csv)
    next(leitor_csv)  # pula a linha de cabeçalho
    for linha in leitor_csv:
        chave = linha[indice_coluna_chave]
        dicionario[chave] = linha
    arquivo_csv.close()
    return dicionario


def main():
    
    NOME_LOJA = "Empório Inkom"
    ALIQUOTA_IMPOSTO = 0.06

    INDICE_PRODUTO = 0
    INDICE_NOME = 1
    INDICE_PRECO = 2

    try:
        dic_produtos = ler_dicionario("produtos.csv", INDICE_PRODUTO)

        arquivo_pedido = open("pedido.csv", "r", encoding="utf-8")
        leitor_pedido = csv.reader(arquivo_pedido)
        next(leitor_pedido)  # pula a linha de cabeçalho (Produto #, Quantidade)

        print(NOME_LOJA)

        numero_itens = 0
        subtotal = 0

        for linha in leitor_pedido:
            numero_produto = linha[0]
            quantidade = int(linha[1])

            info_produto = dic_produtos[numero_produto]
            nome_produto = info_produto[INDICE_NOME]
            preco_produto = float(info_produto[INDICE_PRECO])

            print(f"{nome_produto}: {quantidade} @ {preco_produto:.2f}")

            numero_itens += quantidade
            subtotal += quantidade * preco_produto

        arquivo_pedido.close()

        imposto = subtotal * ALIQUOTA_IMPOSTO
        total = subtotal + imposto

        print(f"Número de itens: {numero_itens}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Imposto sobre vendas: {imposto:.2f}")
        print(f"Total: {total:.2f}")
        print(f"Obrigado por comprar no {NOME_LOJA}.")

        agora = datetime.now()
        print(agora.strftime("%d/%m/%Y %H:%M:%S"))

    except FileNotFoundError as erro:
        print("Error: missing file")
        print(erro)
    except PermissionError as erro:
        print("Error: permission denied")
        print(erro)
    except KeyError as erro:
        print(f"Error: unknown product ID in the request.csv file {erro}")

if __name__ == "__main__":
    main()