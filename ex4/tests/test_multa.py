import pytest
from multa import valor_com_multa
def test_valor_com_multa_avl():
    with pytest.raises(ValueError, match="atraso invalido"):
        valor_com_multa(100.0, -1) 
    assert valor_com_multa(100.0, 0) == 100.0 
    assert valor_com_multa(100.0, 1) == 100.0 

    assert valor_com_multa(100.0, 4) == 100.0 
    assert valor_com_multa(100.0, 5) == 100.0 
    assert valor_com_multa(100.0, 6) == 101.0 
    assert valor_com_multa(100.0, 7) == 102.0 

    assert valor_com_multa(100.0, 59) == 154.0 
    assert valor_com_multa(100.0, 60) == 155.0 
    with pytest.raises(ValueError, match="atraso invalido"):
        valor_com_multa(100.0, 61) 

def test_mutantes_remanescentes():
    # Mata o mutante 7 
    with pytest.raises(ValueError) as excinfo:
        valor_com_multa(100.0, -1)
    assert str(excinfo.value) == "atraso invalido"

    # Mata os mutantes (23, 25, 26)
    assert valor_com_multa(33.33, 7) == 34.0

def test_arredondamento_preciso():
    assert valor_com_multa(101.0, 6) == 102.01

'''
Questoes:

a) Sem rodar nenhuma ferramenta, escreva uma suíte por análise de
valor-limite (aula 6)
    R: codigo.

b) Meça a cobertura de ramos e o MS dessa suíte
    R: Cobertura de ramos 100%. MS: 80,77%

c) Para cada vivo, escreva um teste que o mate ou justifique por que é
equivalente. Informe o MS final
    R: MS final: 100% (mesmo com o mutante 9 ainda vivo)

d) Escolha dois mutantes de primeira ordem que sua suíte mata. Aplique
as duas mudanças juntas, à mão, no código
    R: Mudado.

e) Rode a suíte contra esse mutante de segunda ordem. Ela o mata?
Relacione com o efeito de acoplamento e com Offutt (1992)
    R: Mata. A relação se da por testes que sao focados em mutações simples são altamente eficazes para pegar defeitos copostos do mundo real.

'''