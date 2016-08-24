# python-bdd-compare

A ideia desse repositório é fazer uma comparação de diferentes frameworks de [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) em python

Pretendo tomar como referência os testes unitários disponíveis na biblioteca padrão do python e comparar a complexidade de escrita de testes e reports dados pelos frameworks.

### Frameworks escolhidos

[Behave](behave/impressoes.md)

[~~Lettuce~~](lettuce/impressoes.md) (Não tem suporte a python3)

[Pycukes](pycukes/impressoes.md)

[Pytest-bdd](pytest-bdd/impressoes.md)

[Radish](radish/impressoes.md)

### Ambiente para execução das comparações

| Sistema    | Versão     |
|   ----     |      ---   |
| SO         | ArchLinux  |
| Python     | 3.5.2      |

### Versões dos frameworks
| framework  | Versão     |
|   ----     |      ---   
| Behave     | 1.2.5      |
| Lettuce    | 0.2.23     |
| Pycukes    | 0.2        |
| Pytest-bdd | 2.17.1     |
| Radish     | 0.2.10     |

### Teste 1 - Diferenças em uma implementação simples

Quando entrar na página do python, usando selenium, a palavra python deve estar no título

`assert Python in driver.title == True`

[unittest](unittest/teste_1.py) - 17 linhas

[Behave](behave/teste_1.py) - 29 linhas (17=py, 12=feature)

Lettuce - Não ofereceu suporte a python3

#### Resultados
