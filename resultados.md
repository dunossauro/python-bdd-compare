### Teste 1 - Diferenças em uma implementação simples

Quando entrar na página do python, usando selenium, a palavra python deve estar no título

`assert Python in driver.title == True`

#### Resultados
[unittest](unittest/teste_1.py) - 17 linhas

[Behave](behave/teste_1.py) - 29 linhas (17=py, 12=feature)

Lettuce - Não ofereceu suporte a python3

pycukes - Encontrei problemas na execução e abri uma [issue](https://github.com/hltbra/pycukes/issues/9) no projeto.

[Pytest](pytest-bdd/teste_1) - 34 linhas (25=py, 9=feature)
