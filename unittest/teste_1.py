from unittest import TestCase, main
from selenium import webdriver


class teste(TestCase):
    """
    Funcionalidade: A palavra python existe na descrição do site

    O contexto é definido implicitamente na classe de testes por self
    """
    ff = webdriver.Firefox()
    ff.get("https://www.python.org/")

    def teste_driver(self):
        """
        Dado que o browser esteja na pagina do python
        """
        self.assertEqual(self.ff.current_url,
                         "https://www.python.org/")

    def teste_page(self):
        """
        Então Python deve estar no título
        """
        self.assertIn("Python", self.ff.title)
        self.ff.close()


if __name__ == '__main__':
    main()
