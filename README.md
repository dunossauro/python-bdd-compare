# Pythons e os frameworks de [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development)

A ideia desse repositório é fazer uma comparação de diferentes frameworks de BDD em python e como o foco é realmente escolher uma ferramenta para uso próprio, no fim dos 10 testes, vou detalhar como foi a minha experiência com cada um deles e fazer um top 5 levando em consideração alguns pontos que vou definir no meio do processo.

Pretendo também fazer análises não só de linhas de código, pois o estado da documentação é importante, tanto quanto a atividade dos repositórios e os reports oferecidos por cada ferramenta.

### Como isso vai funcionar?

Como não vivemos só de flores e as documentações as vezes são muito complexas, vou começar tentando executar um teste extremamente simples, antes de ler documentações e olhar os reports. Por que? Como nesse escopo vou selecionar apenas ferramentas que oferecem suporte a python 3, alguma delas pode ser descartada no primeiro import. Sei que as documentações costumam apontar a que versão dão suporte etc... Mas caso as coisas se mostrem muito complexas logo de cara, e a ideia do bdd é ser simples, os testes podem não valer a pena.

Executando esses primeiros testes já podemos ver os caminhos que vamos traçar e, caso aconteça, podemos descartar algumas ferramentas, ou não, logo no começo sem extender muita leitura de documentação desnecessária.

### Por que testar tantas ferramentas, você está louco?

Não. Eu realmente passei mal uns bocados quando tive que mudar minha visão de mundo de desenvolvedor para tester e sei que isso pode ajudar pessoas a percorrer o caminho das pedras. Não só na conversão dev/test, mas as vezes procuramos algo simples, em português e não se encontra nada. E lidar com frameworks que não são estáveis, todos são muito jovens, tanto o Radish, Lettuce e o Pycuckes não estão nem na primeira versão estável(1.0), é sempre complicado. A Ferramenta mais madura, olhando a nível de Números é o pytest-bdd (2.17), mas ele também é um plugin do pytest e se apoia nos recursos do mesmo, o que pode oferecer alguma vantagem pra quem já possua conhecimentos no framework, mas pode oferecer uma péssima experiência pra quem possui conhecimentos no [cucumber](https://cucumber.io/) que é a referência dos frameworks de BDD.

Então temos que levar em consideração todos esse pontos na hora de escolher um framework que vai ser responsável por fazer nosso trabalho. Afinal, programar tem que ser sempre uma experiência prazerosa, se gostassemos de coisas confusas e com alto nível de complexidade não estariamos falando de python

### algumas considerações finais:

O ambiente em que executei esses testes está descrito [aqui](docs/ambiente.md).

E, para finalizar, adescrição dos testes, um a um, vai estar [nesse documento](docs/testes.md) e  os resultados parcialmente serão inseridos [aqui](docs/resultados.md)

### Frameworks escolhidos

[Behave](https://github.com/behave/behave)

[Lettuce](https://github.com/gabrielfalcao/lettuce)

[Pycukes](https://github.com/hltbra/pycukes)

[Pytest-bdd](https://github.com/pytest-dev/pytest-bdd)

[Radish](http://radish-bdd.io/)


## [impressões finais](docs/impressoes_finais.md)
