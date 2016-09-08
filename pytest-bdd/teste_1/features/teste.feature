Feature: A palavra python existe na descrição do site

    Background: preparando o ambiente
        Given setar o browser no selenium
        And entrar em https://www.python.org/

    Scenario: Verificar se python está no título do site
        Given que o browser esteja na pagina https://www.python.org/
        Then a palavra Python deve estar no titulo
