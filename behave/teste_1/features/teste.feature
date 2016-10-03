# language: pt

Funcionalidade: A palavra python existe na descrição do site

    Contexto: preparando o ambiente
        Quando setar o browser no selenium
        Então entrar em "https://www.python.org/"

    Cenário: Verificar se python está no título do site
        Dado que o browser esteja na pagina "https://www.python.org/"
        Então a palavra "Python" deve estar no titulo
