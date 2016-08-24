# Lettuce

Logo no primeiro teste tive a triste resposta de um erro em um print:

```
File "/usr/lib/python3.5/site-packages/lettuce/__init__.py", line 179
  print "Error loading step definitions:\n", e
                                          ^
SyntaxError: Missing parentheses in call to 'print'

```

Depois de procurar um pouco, por não fica explicito no site official do lettuce ([link](http://lettuce.it/)), achei uma [issue](https://github.com/gabrielfalcao/lettuce/issues/458) no [github do projeto](https://github.com/gabrielfalcao/lettuce) que diz que o Gabriel Falcão, desenvolvedor projeto, está trabalhando (Dec 2015) para que funcione no python3. Como uso arch linux e o Python3 é o default do meu sistema, tive algumas dificuldades e rodar o projeto, mas o teste acabou rolando. Embora tenha funcionado, o meu cenário para os testes é baseado em python3
