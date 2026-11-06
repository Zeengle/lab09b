import pytest
from cotacoes import menor_preco, dia_da_compra


def test_menor_preco():
    assert menor_preco([32, 28, 35, 25, 30]) == 25
    assert menor_preco([40]) == 40
    assert menor_preco([20, 27]) == 20
    # Mata o mutmut_7
    assert menor_preco([30, 10, 50]) == 10


def test_dia_da_compra():
    assert dia_da_compra([32, 28, 35, 25, 30]) == 3
    assert dia_da_compra([40]) == 0
    assert dia_da_compra([20, 27]) == 0
    # Mata o mutmut_11
    assert dia_da_compra([30, 10, 50]) == 1
    # Mata o mutmut_12
    assert dia_da_compra([10, 20, 10]) == 2


def test_cotacoes_vazias():
# Mata os mutantes 2, 3, 4 em ambas as funções
    with pytest.raises(ValueError) as excinfo:
        menor_preco([])
    assert str(excinfo.value) == "sem cotacoes"

    with pytest.raises(ValueError) as excinfo:
        dia_da_compra([])
    assert str(excinfo.value) == "sem cotacoes"


'''
Questoes:

a) Escreva essa suíte e rode o mutmut. Veja a mudança de cada vivo com
o mutmut show
    R: Mutantes 2,3 e 4 das duas funções alteram o texto do erro. 
    O mutante menor_preco 7, dia_compra 9 e 11 mudaram os indices de inicio da varredura. 
    E os mutantes menor_preco 8 e dia_compra 12 trocaram < por <= ou vice versa

b) Classifique cada vivo como equivalente ou não equivalente. Justifique
pela especificação da função
    R:mutantes 2, 3 e 4 de ambas as funções: Não equivalentes (Alterara a mensagem de erro modifica o contrato da exceção)
    Mutante menor_preco 7: Não equivalente (pular o primeiro elemento apos o inicial altera a logica de varredura).
    Mutante menor_preco 8: Equivalente (qualquer entrada numerica. < e <= produzem exatamente o mesmo resultado final de menor preco).
    Mutante dia_compra 9: Equivalente (Iniciar o loop em 0 faz a primeira iteração sempre verdadeira)
    Mutante dia_compra 11: Não Equivalente (Começar o loop pelo indice 2 faz o elemento do indice 1 seja ignorado)
    Mutante dia_compra 12: Não Equivalente (Faz com que a funçã retorne o primeiro dia do empate, alterando o comportamento semantico da função)

c) Escreva testes que matem os não equivalentes. Calcule o MS antes e
depois desses testes
    R: Antes: 81.82%. Depois: 100% (pois os 2 mutantes restantes são equivalentes)

d) Trocar < por <= em menor_preco gera um equivalente. Trocar <= por <
em dia_da_compra não gera. Explique
    R: Porque o menor_preco usa um valor numerico e o dia_da_compra utiliza um indice/posição. Fazendo assim o resultado ser distinto em ambas

'''