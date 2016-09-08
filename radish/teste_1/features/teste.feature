#@constant(python : "https://www.python.org/")
Feature: A palavra python existe na descricao do site

    Background: preparando o ambiente
        Given setar o browser no selenium
        Given entrar no site do python

    # #@precondition(teste.feature: preparando o ambiente)
    Scenario: Verificar se python esta no titulo do site
        Given que o browser esteja na pagina python
        Then a palavra Python deve estar no titulo
