from cashback import cashback

def test_cashback():
    assert cashback([50,100,200]) == 15.0

# adição para 100% MS
def test_cashback_arredondamento():
    assert cashback([333.33]) == 16.67

'''
Questoes

a) Meça a cobertura de ramos e o MS. Explique por que os dois números
são tão diferentes
    R:Cobertura dos ramos: 100%. MS = 23,08%. 
    Os numeros são diferentes porque medem coisas distintas. A cobertura de ramos mede apenas a execução e o MS mede a sensibilidade das asserções.

b) Troque o > 0 pelo valor exato esperado, com a mesma lista de
compras. Quantos mutantes continuam vivos?
    R: 3 Mutantes continuam vivos.

c) Para cada mutante que continuou vivo, diga qual condição não foi
atendida: alcançar, infectar, propagar ou revelar
    R: Os 3 alteram o arredondamento para None, vazio ou 3 decimais. A condição não atendida foi a Revelar porque 15.0 arredondado para 3 casas, None ou um padrão, continua sendo 15.0 fazendo o teste passar e o mutante sobreviver.

d) Acrescente casos de teste até o MS chegar a 100%. Que característica a
nova entrada precisou ter?
    R: A nova entrada precisou ser maior ou igual a 100 e que gera mais de duas casas decimais.

'''