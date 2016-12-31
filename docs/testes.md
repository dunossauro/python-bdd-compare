# Testes e resultados

## Teste 1 - Diferenças em uma implementação simples

Nesse teste vamos somente abrir o browser e fazer uma validação usando selenium:

Quando entrar na página do python, a palavra Python deve estar no título

`assert Python in driver.title == True`

Nesse teste pretendo pontuar a complexidade de escrever um teste simples e a quantidade de linhas de código que vamos levar pra escrever o mesmo.

Pontos:

| Colocado | nº de linhas | simplicidade |
| -------- | ------------ | ------------ |
| 1º | 3 | 5 |
| 2º | 2 | 3 |
| 3º | 1 | 1 |

### Impressões

A conclusão que consigo tirar de rodar o mesmo teste em tantas plataformas diferentes é que os pequenos detalhes são os que mais contam.

Estou realmente habituado a escrever testes usando unittest e o behave. Como combinado a comparação era sempre em relação a simplicidade de rodar testes usando o unittest que não é a melhor base de comparação, nós todos sabemos. Testes funcionais raramente vão ter efeitos positivos usando unittest. Então, sem mais delongas, as impressões de todos os frameworks:

* Behave:


Consigo enxergar que o behave, mesmo que superficialmente, tem um start bem básico para quem não sabe nada na documentação, mas não iremos falar de documentação, então...
No quisito de estruturar os arquivos e ter a opção de background, achei que a dinâmica do behave flui melhor pra quando estamos escrevendo features. As coisas se dão de uma maneira muito simples no código:

```python
from behave import step

#Quando - When
@step('comer "{n}" maçãs')
def test(context, n):
    pass
```
podendo definir todos os steps com o decorador `@step` me sinto menos preso a determinadas situações que me encontrei em outros frameworks como pytest ou ao radish.

Quanto o gherkin não encontrei muitas funções diferentes, ele faz um bom parse usando as variáveis, coisa que não consegui executar nos primeiros testes de outras ferramentas e também aceita português, o que é uma boa saída para os relatórios.

```cucumber
Funcionalidade: Quantas maças consigo comer

    Cenário: -------------
    Quando *****" Variável" *********
    Então %%%%% "Variável" %%%%%%%%%%
```

* pytest-bdd:


Confesso que tive muita dificuldade em rodar esse primeiro teste usando o plugin do pytest. Em quase todos os decoradores de steps tive que usar o parse para fazer o trabalho sujo do pytest-bdd.

```python
from pytest_bdd import parsers, given
@given(parsers.parse('entrar em {site}'))
def ent(site):
    ff.get(site)
```

Qual a dificuldade do framework converter e acessar as posições do dicionário por você?

```python
from parse import parse
from re import compile

regex_0 = compile("\{.*?\}")
regex_1 = compile("\w+")

def pytest_sucks(padrao, entrada):
    elementos = regex_0.findall(padrao)
    chaves = regex_1.findall("".join(elementos))

    dic =  parse(padrao, entrada)
    return dic, chaves

padrao = 'Minha {feature}'

entrada = 'Minha feature'

pytest_sucks(padrao, entrada)

```
Eu também realmente não entendo a necessidade de setar onde estarão os arquivos .feature do projeto, mas pode ser que isso ofereça algumas vantagens. Lí também na documentação do projeto que ele não usam o contexto por não fazerem realmente parte do escopo e o subtituiu pelas proprias fixtures do Pytest, então nos proximos testes exploraremos mais essa funcionalidade


* radish:


Ah... o radish...

Senti algumas coisas diferentes quando executei esse primeiro teste. Primeira: Estou muito acostumado com o behave. Tive uma dificuldade em entender que não existe um `Background`, mas existe o `precondition` e realmente essas funcionalidades que o radish por trás no gherkin são fenomenais. Não quero entrar nesse mérito, mas veremos mais disso em outros testes.

```cucumber
Feature: A palavra python existe na descricao do site
    @precondition(preparar.feature: preparando o ambiente)
```

Segundo: Uma coisa que achei meio estranha e talvez os hooks resolvam é a de que dois cenários não compartilham o mesmo contexto, coisa que uso habitualmente no behave.

No mais, me senti falta dos steps serem em português, acabei me empolgando e mandando um [pull request](https://github.com/radish-bdd/radish/pull/23) para o projeto e tenho certeza que nas proximas versões podemos contar com esse recurso. Também encontrei dificuldades em fazer o parse das features usando o radish, assim como no pytest-bdd. Mas não acho um problema tão grave quando comparado ao numeros de releases que existem do pytest quando comparadas ao radish. A solução foi criar dicionários para resolver o problema

```python
dic = {"python" : "https://www.python.org/"}

@given("que o browser esteja na pagina {site:w}")
def test(step, site):
    assert step.context.ff.current_url == dic[site]
```

Pra finalizar me senti um pouco preso, mas muito livre. Controverso, não? Apesar de os step (Given, Then, When) necessariamente terem que ser declarados nas funções, sei que existe um método mais simples pra fazer isso. Embora não seja tão funcional quanto o do behave. Mas me senti tão livre quando soube que o gherkin não serve apenas para linguagem natural e tem cartas na manga.


* Lettuce


Talvez de todos, o lettuce, seja o que tenha me deixado mais decepcionado. A documentação é bem bacana, é mantido por um brasileiro. Mas em que lugar da documentação conta que ele não roda em python 3? Nenhum. Como não faz parte do meu escopo, vou acabar abandonando o Lettuce nesse primeiro teste. Para saber mais sobre o ocorrido [clique aqui](../lettuce/impressoes.md)

* pycukes


Com o  Pycukes eu não consegui nem executar e conto sobre isso [aqui](../pycukes/impressoes.md)

### pontos

Os resultados podem ser vistos [aqui](./resultados.md)


Em números de linhas:

1. Behave (3p)
2. Radish (2p)
3. Pytest-bdd (1p)

Em simplicidade:

1. Behave (5p)
2. Radish (3p)
3. Pytest-bdd (1p)

## Teste 2 - Documentação

Essa parte da comparação é a que considero mais importante. Todos os frameworks são muitos jovems e o próprio cucumber, pioneiro no assunto, surgiu em [2008](https://www.infoq.com/news/2015/03/bdd-cucumber-testing), então não temos uma literatura vasta no assunto. Na verdade são pouquissimos livros que falam sobre frameworks de BDD.

Então, só podemos aprender de duas maneiras:
* Com alguém nos ensinando o que conseguiu extrair das documentações; ou
* Lendo a porra da documentação ([RTMF](https://en.wikipedia.org/wiki/RTFM))

Com isso, pretende-se abordar cinco tópicos diferentes nas documentações:

1. Um quickstart
2. Clareza na documentação
3. Documentação da implementação (classes, atributos, funções, código em geral)
4. Exemplos de uso
5. Uma busca eficiente (Quase sempre são sites, então uma boa busca pode retornar resultados exatos sobre o que estamos procurando)

Pontos:

| Colocado | Quickstart | Clareza | Implementação | Exemplos | Busca |
| -------- | ------------ | ------------ | --------- | ----------- | --------- |
| 1º | 3 | 5 | 3 | 2 | 1 |
| 2º | 2 | 3 | 2 | 1 | 0 |
| 3º | 1 | 1 | 1 | 0 | 0 |

### Impressões

### pontos


## Teste 3 - Contexto (parte 1)

O teste 3 consiste em uma simples utilização do contexto. No unittest o contexto já é explicito e simples de usar com self. o argumento 'step' já tinha sido usado no primeiro teste com radish. E, no behave, também já foi usado com 'context'. Mas o que quero demonstrar nesse teste em expecífico é a utilização dos mesmos, pois existem arquivos e locais expecíficos para a utilização universal dos mesmos, diferente do unittest que faz isso simplesmente utilizando a classe.

Esse teste não tem um 'produto final' pois ele não executa um 'teste', na verdade vamos testar o uso do contexto.

O que pode ser avaliado aqui é a simplicidade em que os frameworks lidam com compartilhamento de 'atributos', funções e tudo que é possível compartilhar.

Pontos:

### Impressões

### pontos

Em números de linhas:

Em simplicidade:

## Teste 4 - Hooks

Pontos:


### Impressões

### pontos

Em números de linhas:

Em simplicidade:

## Teste 5 - Arquivo Gherkin (de features)

Pontos:


### Impressões

### pontos

Em números de linhas:

Em simplicidade:

## Teste 6 - Contexto (parte 2)

Esse teste chega a ser muito parecido com o teste 3, sem nenhuma aplicação visível, mas vamos deixar um pouco mais complexa e com mais arquivos a utilização do contexto.


Pontos:


### Impressões

### pontos

Em números de linhas:

Em simplicidade:

## Teste 7 - um teste com média complexidade

Pontos:


### Impressões

### pontos

Em números de linhas:

Em simplicidade:


## Teste 8 - Ecossistema do framework (integrações com outras ferramentas)

Pontos:


### Impressões

### pontos

Em números de linhas:

Em simplicidade:

## Teste 9 - Reports

Pontos:


### Impressões

### pontos

Em números de linhas:

Em simplicidade:

## Teste 10 - Um teste com "alta" complexidade

Pontos:


### Impressões

### pontos

Em números de linhas:

Em simplicidade:
