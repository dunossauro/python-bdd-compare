Feature: A palavra python existe na descricao do site

    @precondition(preparar.feature: preparando o ambiente)
    Scenario: Verificar se python esta no titulo do site
        Given que o browser esteja na pagina python
        Then a palavra Python deve estar no titulo
