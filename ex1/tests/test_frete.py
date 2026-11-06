import pytest
from frete import modalidade_frete

# def test_modalidade_frete_inicial():
#     assert modalidade_frete(5, 300) == "Correio expresso"
#     assert modalidade_frete(2, 1000) == "Correio economico"

# adicionando para matar os vivos
def test_peso_invalido():
    with pytest.raises(ValueError, match="Peso invalido"):
        modalidade_frete(0, 100)
    with pytest.raises(ValueError, match="Peso invalido"):
        modalidade_frete(-1, 100)
    with pytest.raises(ValueError, match="Peso invalido"):
        modalidade_frete(31, 100)


def test_distancia_invalida():
    with pytest.raises(ValueError, match="Distancia invalida"):
        modalidade_frete(5, -1)
    with pytest.raises(ValueError, match="Distancia invalida"):
        modalidade_frete(5, 5001)


def test_transportadora():
    assert modalidade_frete(21, 100) == "Transportadora"
    assert modalidade_frete(30, 100) == "Transportadora"


def test_motoboy():
    assert modalidade_frete(5, 0) == "Motoboy"
    assert modalidade_frete(5, 10) == "Motoboy"


def test_correio_expresso():
    assert modalidade_frete(5, 11) == "Correio expresso"
    assert modalidade_frete(5, 300) == "Correio expresso"
    assert modalidade_frete(5, 500) == "Correio expresso"


def test_correio_economico():
    assert modalidade_frete(5, 501) == "Correio economico"
    assert modalidade_frete(5, 5000) == "Correio economico"
    assert modalidade_frete(2, 1000) == "Correio economico"


'''
Questoes:
a) Meça a cobertura de ramos e rode o mutmut. Informe a cobertura e
quantos mutantes foram gerados, mortos e vivos
    R: Cobertura de 64%, gerando 36 mutações onde 6 estão mortos e 30 vivos.

b) Agrupe os vivos pelo trecho do código que cada um altera. Indique
quais estão em linhas que a suíte não executa
    R:Linha 3: Mutantes 6 a 9. 
    Linha 5: Mutantes 15 a 18. 
    Linha 7: Mutantes 21 a 23. 
    Linha 9: Mutantes 26 a 28.

c) Acrescente testes até matar os vivos. Se algum não puder ser morto,
justifique por que é equivalente. Informe o MS final
    R: Não teve mutantes vivos. MS: 100%

d) Nos testes de exceção, troque str(erro.value) == msg por
pytest.raises(ValueError, match=msg). Rode o mutmut de
novo e explique a diferença no MS
    R:  o MS ficou de 88.89%. São equivalentes porque o parametro match = do pytest.raises utiliza busca padrão e nao verifica a igualdade exata.

'''