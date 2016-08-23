from unittest import TestCase, main
from selenium import webdriver


# ----- Funcionalidade: A palavra python existe na descrição do site
class teste(TestCase):
    # ----- Contexto
    ff = webdriver.Firefox()
    ff.get("https://www.python.org/")

    # ----- Dado que o browser esteja na pagina do python
    def teste_driver(self):
        self.assertEqual(self.ff.current_url,"https://www.python.org/")

    # ----- Então Python deve estar no título
    def teste_page(self):
        self.assertIn("Python", self.ff.title)
        self.ff.close()

if __name__ == '__main__':
    main()
