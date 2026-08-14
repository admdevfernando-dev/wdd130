"""
Controle-almoxarife - Sistema de Controle de Estoque de Almoxarifado
Programa de linha de comando para cadastrar itens, registrar entradas e
saídas de material, e avisar quando um item está com estoque baixo.
"""
import csv
import os
import sys
from datetime import datetime

ARQUIVO_ESTOQUE = "estoque.csv"
ARQUIVO_MOVIMENTACOES = "movimentacoes.csv"
CABECALHO_ESTOQUE = ["codigo", "nome", "quantidade", "unidade", "quantidade_minima"]


def carregar_estoque(caminho_arquivo=ARQUIVO_ESTOQUE):
    
    estoque = []
    if not os.path.exists(caminho_arquivo):
        return estoque
    with open(caminho_arquivo, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            estoque.append({
                "codigo": linha["codigo"],
                "nome": linha["nome"],
                "quantidade": int(linha["quantidade"]),
                "unidade": linha["unidade"],
                "quantidade_minima": int(linha["quantidade_minima"]),
            })
    return estoque


def salvar_estoque(estoque, caminho_arquivo=ARQUIVO_ESTOQUE):
    
    with open(caminho_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CABECALHO_ESTOQUE)
        escritor.writeheader()
        for item in estoque:
            escritor.writerow(item)


def validar_quantidade(valor):
    
    try:
        numero = int(valor)
    except (ValueError, TypeError):
        return False
    return numero > 0


def buscar_item(estoque, termo):
    
    termo = str(termo).strip().lower()
    for item in estoque:
        if item["codigo"].lower() == termo or item["nome"].lower() == termo:
            return item
    return None


def adicionar_item(estoque, codigo, nome, quantidade, unidade, quantidade_minima):
    
    if buscar_item(estoque, codigo) is not None:
        return False
    if not validar_quantidade(quantidade) or not validar_quantidade(quantidade_minima):
        return False
    estoque.append({
        "codigo": str(codigo),
        "nome": str(nome),
        "quantidade": int(quantidade),
        "unidade": str(unidade),
        "quantidade_minima": int(quantidade_minima),
    })
    return True


def registrar_movimentacao(tipo, codigo, quantidade, caminho_arquivo=ARQUIVO_MOVIMENTACOES):
    
    arquivo_novo = not os.path.exists(caminho_arquivo)
    with open(caminho_arquivo, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        if arquivo_novo:
            escritor.writerow(["data_hora", "tipo", "codigo", "quantidade"])
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        escritor.writerow([data_hora, tipo, codigo, quantidade])


def registrar_entrada(estoque, codigo, quantidade):
    
    item = buscar_item(estoque, codigo)
    if item is None or not validar_quantidade(quantidade):
        return None
    item["quantidade"] += int(quantidade)
    registrar_movimentacao("entrada", item["codigo"], int(quantidade))
    return item["quantidade"]


def registrar_saida(estoque, codigo, quantidade):
    
    item = buscar_item(estoque, codigo)
    if item is None or not validar_quantidade(quantidade):
        return None
    if int(quantidade) > item["quantidade"]:
        return None
    item["quantidade"] -= int(quantidade)
    registrar_movimentacao("saida", item["codigo"], int(quantidade))
    return item["quantidade"]


def listar_itens(estoque):
    
    if not estoque:
        return "Nenhum item cadastrado."
    linhas = [f"{'CÓDIGO':<10}{'NOME':<22}{'QTD':<8}{'UNIDADE':<10}{'QTD MÍN':<8}"]
    for item in estoque:
        linhas.append(
            f"{item['codigo']:<10}{item['nome']:<22}{item['quantidade']:<8}"
            f"{item['unidade']:<10}{item['quantidade_minima']:<8}"
        )
    return "\n".join(linhas)


def verificar_estoque_baixo(estoque):
    
    return [item for item in estoque if item["quantidade"] < item["quantidade_minima"]]


def exibir_menu():
    
    print("\n===== Controle-almoxarife - Controle de Estoque =====")
    print("1. Cadastrar novo item")
    print("2. Registrar entrada de material")
    print("3. Registrar saída de material")
    print("4. Buscar item")
    print("5. Listar todos os itens")
    print("6. Verificar itens com estoque baixo")
    print("0. Sair")
    return input("Escolha uma opção: ").strip()


def main():
    
    estoque = carregar_estoque()

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            codigo = input("Código do item: ").strip()
            nome = input("Nome do item: ").strip()
            quantidade = input("Quantidade inicial: ").strip()
            unidade = input("Unidade de medida (ex.: un, cx, kg): ").strip()
            quantidade_minima = input("Quantidade mínima: ").strip()
            if adicionar_item(estoque, codigo, nome, quantidade, unidade, quantidade_minima):
                salvar_estoque(estoque)
                print("Item cadastrado com sucesso!")
            else:
                print("Não foi possível cadastrar (código repetido ou dado inválido).")

        elif opcao == "2":
            codigo = input("Código do item: ").strip()
            quantidade = input("Quantidade a adicionar: ").strip()
            resultado = registrar_entrada(estoque, codigo, quantidade)
            if resultado is not None:
                salvar_estoque(estoque)
                print(f"Entrada registrada. Nova quantidade: {resultado}")
            else:
                print("Não foi possível registrar a entrada (item não encontrado ou quantidade inválida).")

        elif opcao == "3":
            codigo = input("Código do item: ").strip()
            quantidade = input("Quantidade a retirar: ").strip()
            resultado = registrar_saida(estoque, codigo, quantidade)
            if resultado is not None:
                salvar_estoque(estoque)
                print(f"Saída registrada. Nova quantidade: {resultado}")
            else:
                print("Não foi possível registrar a saída (item não encontrado, quantidade inválida ou insuficiente).")

        elif opcao == "4":
            termo = input("Digite o código ou nome do item: ").strip()
            item = buscar_item(estoque, termo)
            print(f"Encontrado: {item}" if item else "Item não encontrado.")

        elif opcao == "5":
            print(listar_itens(estoque))

        elif opcao == "6":
            baixos = verificar_estoque_baixo(estoque)
            if baixos:
                print("Itens com estoque abaixo do mínimo:")
                print(listar_itens(baixos))
            else:
                print("Nenhum item está com estoque baixo.")

        elif opcao == "0":
            print("Encerrando o Controle-almoxarife. Até logo!")
            sys.exit(0)

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
