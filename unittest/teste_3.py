from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

elementos = {'busca': 'id-search-field'}


class teste(TestCase):
    """
    Fica simples e óbvia a aplicação do contexto quando usa-se classes
        por exemplo:

        A classe já tem um esquema de monkey patch definido em self.
        Pode-se atribuir qualquer coisa em self e o mesmo pode ser usado
        em qualquer parte da classe.
    """
    ff = webdriver.Firefox()
    url = 'http://python.org'
    e = elementos

    def test_1(self):
        """
        self nesse caso contém tudo que foi inserido em TestCase
        a classe que foi herdada e também ff, o driver do firefox, e url
        """
        self.ff.get(self.url)

    def test_2(self):
        """
        Pode-se usar o dicionário que define a posição dos elementos na tela
        """
        self.busca = self.ff.find_element_by_id(self.e['busca'])
        self.busca.clear()
        self.busca.send_keys('collections')
        self.busca.send_keys(Keys.RETURN)

    def test_3(self):
        """
        Só pra fechar o browser
        """
        self.ff.quit()


if __name__ == '__main__':
    main()
