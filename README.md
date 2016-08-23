# python-bdd-compare

A ideia desse repositório é fazer uma comparação de diferentes frameworks de [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) em python

Pretendo tomar como referência os testes unitários disponíveis na biblioteca padrão do python e comparar a complexidade de escrita de testes e reports dados pelos frameworks.

### Teste 1 - Diferenças em uma implementação simples

Quando entrar na página do python, usando selenium, a palavra python deve estar no título

`assert Python in driver.title == True`

[unittest](unittest/teste_1.py) - 21 linhas
