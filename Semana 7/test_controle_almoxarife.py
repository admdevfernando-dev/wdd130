"""
Arquivo de testes do programa Controle-almoxarife.
Cada função de teste chama as funções do programa principal pelo menos
duas vezes e usa pelo menos duas instruções assert para validar o
resultado.
"""

from controle_almoxarife import (
    adicionar_item,
    registrar_entrada,
    registrar_saida,
    buscar_item,
    verificar_estoque_baixo,
    validar_quantidade,
)


def test_validar_quantidade():
    resultado1 = validar_quantidade("10")
    assert resultado1 == True

    resultado2 = validar_quantidade("-5")
    assert resultado2 == False

    resultado3 = validar_quantidade("abc")
    assert resultado3 == False


def test_adicionar_item():
    estoque = []

    resultado1 = adicionar_item(estoque, "001", "Parafuso M6", 100, "un", 20)
    assert resultado1 == True

    resultado2 = adicionar_item(estoque, "001", "Parafuso M6", 50, "un", 20)
    assert resultado2 == False


def test_registrar_entrada():
    estoque = []
    adicionar_item(estoque, "002", "Luva de Proteção", 10, "par", 5)

    nova_quantidade1 = registrar_entrada(estoque, "002", 15)
    assert nova_quantidade1 == 25

    nova_quantidade2 = registrar_entrada(estoque, "999", 5)
    assert nova_quantidade2 is None


def test_registrar_saida():
    estoque = []
    adicionar_item(estoque, "003", "Fita Isolante", 20, "un", 5)

    nova_quantidade1 = registrar_saida(estoque, "003", 8)
    assert nova_quantidade1 == 12

    nova_quantidade2 = registrar_saida(estoque, "003", 100)
    assert nova_quantidade2 is None


def test_buscar_item():
    estoque = []
    adicionar_item(estoque, "004", "Capacete de Segurança", 30, "un", 10)

    item_encontrado = buscar_item(estoque, "004")
    assert item_encontrado is not None

    item_nao_encontrado = buscar_item(estoque, "999")
    assert item_nao_encontrado is None


def test_verificar_estoque_baixo():
    estoque = []
    adicionar_item(estoque, "005", "Óculos de Proteção", 3, "un", 10)
    adicionar_item(estoque, "006", "Máscara Descartável", 200, "un", 50)

    baixos = verificar_estoque_baixo(estoque)
    assert len(baixos) == 1
    assert baixos[0]["codigo"] == "005"


def main():
    test_validar_quantidade()
    test_adicionar_item()
    test_registrar_entrada()
    test_registrar_saida()
    test_buscar_item()
    test_verificar_estoque_baixo()
    print("Todos os testes passaram com sucesso!")


if __name__ == "__main__":
    main()
