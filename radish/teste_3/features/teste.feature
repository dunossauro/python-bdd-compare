Feature: Usar a busca do site do python

    Scenario: Verificar se python esta no titulo do site
        Given entrar no site do python
        When buscar "Collections"
        Then fechar o browser
